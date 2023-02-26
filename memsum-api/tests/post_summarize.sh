#!/bin/bash

curl -X POST localhost:5000/summarize \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 2j4k5sdG" \
 -d@post.json