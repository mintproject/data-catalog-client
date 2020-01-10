dir=${PWD}
parentdir="$(dirname "$dir")"

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i /local/api_doc.json \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json
