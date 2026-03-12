# RoadSense AI API Specification

## Project

RoadSense AI – AI powered road incident detection and reporting platform.


## API Base URL

/api


## API Design Rules

All APIs must return:

status
message
data
timestamp

Response format:

{
 "status":"success",
 "message":"operation completed",
 "data":{},
 "timestamp":"utc time"
}


## Endpoint 1: Upload Incident

POST /api/upload


Description:

Uploads road incident image and metadata.


Input:

multipart form:

image → file

latitude → float

longitude → float


Example request:

image:file

latitude:12.9716

longitude:77.5946


Process flow:

Backend receives file

AWS uploads to S3

AI analyzes image

GPS stored

Record saved

Response returned


Response:

{
 "status":"success",

 "data":{

  "incident_id":"uuid",

  "severity":"medium",

  "image_url":"s3 url",

  "latitude":12.9716,

  "longitude":77.5946

 }

}


## Endpoint 2: Get Potholes

GET /api/potholes


Description:

Returns list of reported incidents.


Response:

{
 "status":"success",

 "data":[

  {

   "id":"uuid",

   "severity":"high",

   "latitude":12.9,

   "longitude":77.5,

   "image_url":"url"

  }

 ]

}


## Endpoint 3: Stats

GET /api/stats


Description:

Returns dashboard statistics.


Response:

{
 "status":"success",

 "data":{

  "total_incidents":120,

  "high_severity":30,

  "medium":60,

  "low":30

 }

}


## AI Service Contract

AI must expose:

analyze_image()

Input:

image path

Output:

{
 "severity":"medium",

 "confidence":85,

 "incident_type":"pothole"

}


## AWS Service Contract

AWS must expose:

upload_image()

store_record()


upload_image output:

{
 "image_url":"s3 link"
}


store_record output:

{
 "record_id":"uuid"
}


## Error Handling

Errors must return:

{
 "status":"error",

 "message":"error reason"
}


## Future APIs

Planned:

GET /api/incident/{id}

POST /api/duplicate-check

POST /api/traffic-impact

POST /api/generate-report


## Versioning

Version:

v1


## Integration Priority

First implement:

POST /api/upload

Then:

GET /api/potholes

Then:

GET /api/stats