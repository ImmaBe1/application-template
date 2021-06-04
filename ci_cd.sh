#!/bin/bash

LOGIN_URL='https://cloud.appscan.com/api/V2/Account/ApiKeyLogin'
UPLOAD_URL='https://cloud.appscan.com/api/v2/FileUpload'
STATIC_SCAN_URL='https://cloud.appscan.com/api/v2/Scans/StaticAnalyzer'
APPSCAN_CLIENT_URL="https://cloud.appscan.com/api/SCX/StaticAnalyzer/SAClientUtil?os="
OS="linux"
APPSCAN_TOOL="$APPSCAN_CLIENT_URL$OS"
GET_SCAN_NAME="CI_CD_VULN_Scan_"
CONTENT_HEADER_JSON='Content-Type:application/json'
ACCEPT_HEADER_JSON='Accept:application/json'
COMMIT_FOLDER="COMMIT_FOLDER"

# Gets API Access Token
function generate-api-token(){
	local token_call="curl --silent -X POST -H '$CONTENT_HEADER_JSON' -H '$ACCEPT_HEADER_JSON' -d '{\"KeyId\":\"${APPSCAN_KEY_ID}\", \"KeySecret\":\"${APPSCAN_KEY_SECRET}\"}' $LOGIN_URL | jq -r '.Token'" 
	eval $token_call
}

# Downloading ASOC Tools
echo "Getting ASOC Tools"
DIR=$(pwd)
FILENAME="$DIR/client.zip"
if [[ ! -f "$FILENAME" ]]; then
	curl --silent -o client.zip $APPSCAN_TOOL
	mkdir client
	mkdir tool
	echo "Unzipping tools"
	unzip -qq client.zip -d client
	cd client ; ls | xargs -I {} sh -c "cp -r {}/* $DIR/tool"
	cd ..
fi

# Copying over commited files for scanning
echo "Preparing commited files for scanning"
CHANGED_FILES=$(git diff --name-only --diff-filter=AM $TRAVIS_COMMIT_RANGE)
DIR=$(pwd)
mkdir $COMMIT_FOLDER
echo "Commited files for scan: "
for file in $CHANGED_FILES ; do \
	echo "$file"
	cp -a $DIR/$file $DIR/$COMMIT_FOLDER ; \
done

# Generating IRX file
echo "Generating IRX file"
DIR=$(pwd)
chmod +x $DIR/tool/bin/..//jre/bin/java
cd $COMMIT_FOLDER
../tool/bin/appscan.sh prepare -oso

# Uploads IRX file
echo "Uploading IRX file"
TOKEN=$(generate-api-token)
AUTH="Authorization: Bearer $TOKEN"
FILE=$(find $(pwd) -maxdepth 2 -name '*.irx' -print)
QUERY="curl --silent -X POST -H 'Content-Type:multipart/form-data' -H '$ACCEPT_HEADER_JSON' -H '$AUTH' -F fileToUpload=@$FILE $UPLOAD_URL"
FILE_DATA=$(eval $QUERY)

#Runs Static Scan
echo "Running Static Scan"
AUTH="Authorization: Bearer $TOKEN"
FILE_ID=$(echo "$FILE_DATA" | jq -r '.FileId')
MY_TIME=$(eval "date +\"%s\"")
SCAN_NAME=$GET_SCAN_NAME$MY_TIME
RUN_SCAN="curl --silent -X POST -H '$CONTENT_HEADER_JSON' -H '$ACCEPT_HEADER_JSON' -H '$AUTH' -d '{\"ARSAFileId\": \"$FILE_ID\", "ApplicationFileId": \"$FILE_ID\", "ScanName": \"$SCAN_NAME\", \"EnableMailNotification\": false, \"Locale\": \"en-US\", \"AppId\": \"$APPSCAN_APP_ID\", \"Execute\": true, \"Personal\": false}' $STATIC_SCAN_URL"
RUN_SCAN=$(eval $RUN_SCAN)

#Prints Scan ID
SCAN_REPORT=$RUN_SCAN
SCAN_ID=$(echo "$SCAN_REPORT" | jq -r .Id)
if [[ "$SCAN_ID" != "null" ]]; then
	echo "SCAN ID: $SCAN_ID"
else
	echo "Could not conduct static scan. Look above for details"
fi