import requests
import json
#import pubchempy


def get_compound_info(cid):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + \
        str(cid) + '/property/MolecularFormula,MolecularWeight,CanonicalSMILES,InChI,InChIKey/JSON'
    r = requests.get(url)
    return r.json()

# Get CID from Name


def get_cid_from_name(name):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + \
        str(name) + '/cids/JSON'
    r = requests.get(url)
    return r.json().get('IdentifierList').get('CID')[0]

# Get CID from CAS


def get_cid_from_cas(cas):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cas/' + \
        str(cas) + '/cids/JSON'
    r = requests.get(url)
    return r.json().get('IdentifierList').get('CAS')[0]


def getHandPfromName(name):
    # name = input("Enter the name of the compound: ")
    cid = get_cid_from_name(name)

    return getHandP(cid)


def getHandP(cid):
    hAndP = [[], []]

    # Get the data from the API
    r = requests.get(
        'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/' + str(cid) + '/JSON/?heading=GHS%20Classification')

    # Convert the data to a dictionary
    data = json.loads(r.text)
    # print(data)

    # Get the GHS classification
    # ['Information'][2]['Value']['StringWithMarkup'][0]['String']

    # Hazard Statements
    try:
        hazards = data['Record']['Section'][0]['Section'][0]['Section'][0]['Information'][2]['Value']['StringWithMarkup']

        for h in hazards:
            hString = h['String']
            hString = hString.split(' ')[0].split(':')[0]
            hAndP[0].append(hString)
            # print(hString)
    except:
        print("No Hazard Statements")

    # Precautionary Statements
    try:
        precautions = data['Record']['Section'][0]['Section'][0]['Section'][
            0]['Information'][3]['Value']['StringWithMarkup'][0]['String']
        precautions = precautions.split(', ')

        for p in precautions:
            p = p.replace('and ', '')
            hAndP[1].append(p)
            # print(p)
    except:
        print("No Precaution Statements")

    return hAndP
