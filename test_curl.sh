# curl -X POST https://api.runpod.ai/v2/hwtrrx02on07n3/runsync \
#     -H 'Content-Type: application/json' \
#     -H 'Authorization: Bearer rpa_ZS8OMILJDSU0UP3PCTDG3VZ5QEUYLKTRDJZEU09Z966i20' \
#     -d '{"input":{"link":"https://testitems.fra1.digitaloceanspaces.com/hu.jpg"}}'


curl -X GET http://localhost:5000/bgtest \
          -H "Content-Type: application/json" \
          -d '{
            "input": {
              "link": "https://testitems.fra1.digitaloceanspaces.com/piz.jpg"
            },
            "uploadTo": {
              "region_name": "fra1",
              "endpoint_url": "https://fra1.digitaloceanspaces.com",
              "aws_access_key_id": "DO00A68ZPATT2M7W6EJF",
              "aws_secret_access_key": "368lcCHa3Xff7LtmN1+Y8tc9p+Pw/86FwpZ507qx2V8",
              "bucket": "rmbg",
              "object_name": "azz.jpg"
            }
          }'