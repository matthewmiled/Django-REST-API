# API To Register Devices

This README information is also displayed in the url path `/api`

## Usage

Responses will be in the format

```json
{
    "data": "Content of response",
    "message": "Description of reponse"
}
```

The following responses will be returned in the `data` field (listed by request type)

___

### GET request to list all devices

**Request**

`GET /api/devices`

**Response**

* `200 OK` on success

```json
[
    {
        "identifier": "bedroom1-tv",
        "name": "Bedroom 1 TV",
        "ip": "111.2.33.4.5",
        "room": "bedroom1"
    },
        {
        "identifier": "lounge-lamp",
        "name": "Lounge Lamp",
        "ip": "111.2.33.4.6",
        "room": "lounge"
    }
]
```
___

### GET request to list specific device details

**Request**

`GET /api/devices/<identifier>`

**Response**

* `404 NOT FOUND` if the device does not exist
* `200 OK` on success

```json
{
    "identifier": "bedroom1-tv",
    "name": "Bedroom 1 TV",
    "ip": "111.2.33.4.5",
    "room": "bedroom1"
}
```
___

### POST request to register new device

**Request**

`POST /api/devices`

**Arguments**

* `"identifier":string` - a unique string for this device
* `"name":string` - a display name for this device
* `"ip":string` - ip address for this device
* `"room":string` - the room that this device is located in

**Response**

* `400 BAD REQUEST` if invalid data posted
* `201 CREATED` on success

```json
{
    "identifier": "bedroom1-tv",
    "name": "Bedroom 1 TV",
    "ip": "111.2.33.4.5",
    "room": "bedroom1"
}
```
___

### DELETE request to delete a device

**Request**

`DELETE /api/devices/<identifier>`

**Response**

* `404 NOT FOUND` if the device does not exist
* `204 NO CONTENT` if delete successful (but nothing useful to return)

___
