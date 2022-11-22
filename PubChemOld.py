import requests
import json
# import pubchempy


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
    try:
        return r.json().get('IdentifierList').get('CID')[0]
    except:
        print("No CID found for " + name)
        return None

# Get CID from CAS


def get_name_from_cid(cid):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + \
        str(cid) + '/property/IUPACName/JSON'
    r = requests.get(url)
    return r.json().get('PropertyTable').get('Properties')[0].get('IUPACName')


def get_cas_from_cid(cid):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + \
        str(cid) + '/property/CAS/JSON'
    r = requests.get(url)
    return r.json().get('PropertyTable').get('Properties')[0].get('CAS')


# print(get_cas_from_cid(2244))


'''
def get_cid_from_cas(cas):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cas/' + \
        str(cas) + '/cids/JSON'
    r = requests.get(url)
    print(r.json())
    return 0  # r.json().get('IdentifierList').get('CAS')[0]

get_cid_from_cas('64-17-5')
'''


def get_H_and_P_from_name(name):
    # name = input("Enter the name of the compound: ")
    cid = get_cid_from_name(name)

    return get_H_and_P(cid)


def get_H_and_P(cid):
    hazardCodes = []
    precautionCodes = []

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
            hazardCodes.append(hString)
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
            precautionCodes.append(p)
            # print(p)
    except:
        print("No Precaution Statements")

    return hazardCodes, precautionCodes


def to_latex_from_name(name):
    cid = get_cid_from_name(name)
    HandP = get_H_and_P(cid)
    print("\\HPStatements{" + str(get_name_from_cid(cid)) +
          "}{\\ghspic{exclam}\\\\\\\\}")
    to_latex(HandP)


def to_latex(HandP):

    print("{\\begin{itemize}")

    # Hazard Statements
    for h in HandP[0]:
        h = h.replace('H', '')
        print("\\item \\ghs{h}{" + h + "}")

    print("\\end{itemize}}")

    # Precautionary Statements
    print("{\\begin{itemize}")
    for p in HandP[1]:
        p = p.replace('P', '')
        print("\\item \\ghs{p}{" + p + "}")

    print("\\end{itemize}}")
    print("{}")


to_latex_from_name(
    input("Enter the name of the compound: ")
)
