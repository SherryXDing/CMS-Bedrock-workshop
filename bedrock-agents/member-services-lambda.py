import json


def return_coverage_summary(beneficiaryID):
    return {
        "beneficiaryID": beneficiaryID,
        "beneficiaryName": "John Doe",
        "age": 67,
        "coverageType": "Medical",
        "parts": [
            "part A",
            "part B",
        ],
        "partADeductible": 100,
        "partBDeductible": 200,
        "partCDeductible": 0,
        "partDDeductible": 0,
        "prescriptionsCovered": False,
        "supplementalInsurance": False,
    }


def return_application_status(beneficiaryID):
    return {
        "beneficiaryId": beneficiaryID,
        "beneficiaryName": "John Doe",
        "applicationNumber": "12345",
        "dateSubmitted": "2020-01-01",
        "applicationType": "Medical",
        "status": "Pending",
        "additionalInfo": "Required paperwork for address verification",
    }


def find_hospitals(location):
    return_list = [
        {
            "providerType": "hospital",
            "providerName": "Hospital 1",
            "providerAddress": "123 Main St",
            "servicesProvided": ["TeleHealth", "Medicare approved payment"],
            "Ratings": 4.5,
        },
        {
            "providerType": "hospital",
            "providerName": "Hospital 2",
            "providerAddress": "123 Frederick St",
            "servicesProvided": ["TeleHealth"],
            "Ratings": 3,
        },
    ]
    return return_list


def find_physicians(location):
    return_list = [
        {
            "providerType": "physician",
            "providerName": "Marsha Jane",
            "providerAddress": "2353 W Main St",
            "servicesProvided": ["Medicare approved payment", "Telehealth"],
            "Ratings": 5,
        },
        {
            "providerType": "physician",
            "providerName": "Melissa Viscomi",
            "providerAddress": "3653 Old National Pike",
            "servicesProvided": ["Medicare approved payment"],
            "Ratings": 2,
        },
    ]
    return return_list


"""
        return_list = [
            {
                "providerType": "pharmacy",
                "providerName": "CVS pharmacy",
                "providerAddress": "2353 E Main St",
                "servicesProvided": ["Medicare approved payment"],
                "providerRatings": 5,
            },
            {
                "providerType": "pharmacy",
                "providerName": "Walgreens",
                "providerAddress": "365 Hopkins St",
                "servicesProvided": ["Medicare approved payment"],
                "providerRatings": 4,
            },
        ]
"""


def lambda_handler(event, context):
    print(event)
    api_path = event["apiPath"]

    if api_path == "/beneficiaries/coverage-summary/{beneficiaryID}":
        parameters = event["parameters"]
        for parameter in parameters:
            if parameter["name"] == "beneficiaryID":
                beneficiaryID = parameter["value"]
                print(beneficiaryID)
        body = return_coverage_summary(beneficiaryID)
        print(body)
    elif api_path == "/beneficiaries/application-status/{beneficiaryID}":
        parameters = event["parameters"]
        for parameter in parameters:
            if parameter["name"] == "beneficiaryID":
                beneficiaryID = parameter["value"]
                print(beneficiaryID)
        body = return_application_status(beneficiaryID)
        print(body)
    elif api_path == "/find-care-providers/hospital/{location}":
        parameters = event["parameters"]
        for parameter in parameters:
            if parameter["name"] == "location":
                location = parameter["value"]
                print(location)
        body = find_hospitals(location)
    elif api_path == "/find-care-providers/physician/{location}":
        parameters = event["parameters"]
        for parameter in parameters:
            if parameter["name"] == "location":
                location = parameter["value"]
                print(location)
        body = find_physicians(location)
    else:
        body = {"{} is not a valid api, try another one.".format(api_path)}

    response_body = {"application/json": {"body": json.dumps(body)}}

    action_response = {
        "actionGroup": event["actionGroup"],
        "apiPath": event["apiPath"],
        "httpMethod": event["httpMethod"],
        "httpStatusCode": 200,
        "responseBody": response_body,
    }

    session_attributes = event["sessionAttributes"]
    prompt_session_attributes = event["promptSessionAttributes"]

    api_response = {
        "messageVersion": "1.0",
        "response": action_response,
        "sessionAttributes": session_attributes,
        "promptSessionAttributes": prompt_session_attributes,
    }

    return api_response
