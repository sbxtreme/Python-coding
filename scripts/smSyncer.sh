#!/bin/bash
#====================================================================================================================================================================================================
# Title          : smSyncer.sh
# Client         : Choice Hotels
# Author         : Shobhit Bhatnagar
# Description    : This is a wrapper script which calls smsyncer CLI. Below are the list of arguments passed in this script
#                                       $1 - api-key (get it from digital properties)
#                                       $2 - secret-key (get it from digital properties)
#                                       $3 - base-url (e.g. https://etl-coordinator.tenant.env.local/)
#                                       $4 - template (e.g. auto-event)
#                                       $5 - file format (csv or json)
#                                       $6 - error dir (dir path where error will be created)
#                                       $7 - filename (e.g. Events.csv)
#                                       $8 - absolute path of filename (e.g. /opt/nifi/data/processor_input/Events_Files/Events.csv)
# Version        : 1.0
# Linux version  : Ubuntu 18.04.4 LTS (Bionic Beaver)
# Example command line:
# ./smSyncer.sh {apikey} {secretkey} {base-url} connect-transaction json /opt/nifi/data/processor_input/error_files test_tran.json /opt/nifi/data/processor_input/transactions/test_tran.json
#=====================================================================================================================================================================================================

#./smSyncer.sh af14e333cf96083199cb680435c367f5cebfe96f 0ab30564c359079db80d6a187fd61c429beffef2 https://etl-coordinator.choicehotels.stg.local/ connect-transaction json /opt/nifi/data/processor_input/error_files test_tran.json /opt/nifi/data/processor_input/transactions/test_tran.json

export HOME=/root;

OUTPUT="$(smsyncer --api-key $1 --secret $2 --base-url $3 job upload $4 --file-format $5 --watch --errors --errors-dir $6/$7 $8 2>&1)"
echo "$OUTPUT"