columnLen = 11
array = []

string = """Hypothalamus 
Neurohypophyse 
Adenohypophyse 
Schilddrüse 
Nebenschilddrüse 
Hormone 
Chemical Class Representative Actions 
Hormones released from the posterior pituitary and 
hormones that regulate the anterior pituitary (see below) 
Oxytoctn 
Antidturetic hormone 
(ADH) 
Growth hormone (GH) 
Prolactin (PRL) 
Folhcle-stimulating 
hormone (FSH) 
Luteinizing hormone 
(LIA) 
Thyroid.stimulating 
hormone (TSH) 
Adrenocorticotropic 
hormone (ACTH) 
Triiodothyronine (Tb) 
and thyroxtne 
Calcitonin 
Parathyroid hormone 
(PTH) 
Peptide 
Peptide 
Protein 
Protein 
Glycopr Otein 
Glycoprotein 
Glycoprotein 
Peptide 
Amine 
Peptide 
Peptide 
Sumulatcs contracuon of 
uterus and mammary gland cells 
Promotes retention of water 
by kidncys 
Stimulates growth (especially 
bones) and metabolic functions 
Sumulates nulk production 
and secretion 
Stimulatcs production of 
ova and sperm 
Stimulates ovaries and testes 
Stimulatcs thyroid gland 
Stimulates adrenal cortex 
to secrete glucocorticoids 
Stimulatc and maintain 
metabohc processes 
Lowers blood calcium levcl 
Raises blood calcium levcl 
Regulated By 
Nervous system 
SVater/salt balancc 
Hypothalamic 
hormones 
Hypothalamic 
hormones 
Hypothalamic 
hormones 
Hypothalamic 
hormones 
Thyroxine in blood: 
hypothalamtc hormones 
Glucocorttcoids; 
hypothalanuc hormones 
TSH 
Calcium in blood 
Calcium in blood
"""

# for i in range(columnLen*4):
#    array.append(input(""))

array = string.splitlines()
print(array)
for line in range(columnLen):
    print(array[line], array[line+columnLen],
          array[line+columnLen*2], array[line+columnLen*3])
