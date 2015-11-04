import pymongo
from pymongo import MongoClient
from pymongo import Connection

class maltiDB:
    #connect to pymongo
    client = MongoClient("localhost", 27017)
    db = client.maltiVerbConjugator

    verbs = []

    connection = MongoClient
    connection = MongoClient()
    db = connection.maltiVerbConjugator
    maltiverb_db = db.maltiVerbConjugator

    #asks for which verb, tense and subject you want
    verb_selector = input("Insert desired verb")
    verb_tense_selector = input("Insert which tense")
    desired_pronoun = input("Insert which subject you want")

    def connect_maltidb():
        """connects to the maltiVerbConjugator database"""
        connection = MongoClient
        connection = MongoClient()
        db = connection.maltiVerbConjugator
        maltiverb_db = db.maltiVerbConjugator
        

#attach the maltiVerbConjugator database to the content of verbs verb_selector
#logic for whether tense is past or present past on user input verb_tense_selector
#logic to retrieve the correct verb on user input verb_selector

#log to choose the subject based on user input
#when user inputs verb, tense and pronoun, look up in database 
 #and return the result of the 3 inputted values



 #how to structure mongo collection to work with verb tenses,
 #pronouns and verb roots
    # entryresult = db.insert_one(
    # {
    # "_id": "ġie",
    # "verbRoot":"ġie",
    #     "verbForms":{
    #     "presentFutureForms": {
    #         "singularForms": {
    #             "jiena": "niġi",
    #             "int":"tiġi",
    #             "hu_huwa": "jiġi",
    #             "hi_hija": "tiġi"
    #     },
    #         "pluralForms": {
    #             "aħna": "niġu",
    #             "intom": "niġu",
    #             "huma": "jiġu"
    #         }},
    #     "pastTenseForms": {
        
    #         "singularForms": {
    #             "jiena": "ġejt",
    #             "int": "ġejt",
    #             "hu_huwa": "ġie",
    #             "hi_hija": "ġiet"
    #         },
    #             "pluralForms": {
    #             "aħna": "ġejtu",
    #             "huma": "ġew"
    #         }}
    # }})

    """Feed the root of the verb, and function will ask you for each form of the verb
   from the first person singular and plurals to imperative forms and inserts the results
   as a document in the database"""

    def verb_insert(root):
        #singular forms
        first_sing_present = input("Type the first person singular form: ")
        second_sing_present = input("Type the second person singular form: ")
        third_sing_he_present = input("Type the third person singular form for 'he': ")
        third_sing_she_present = input("Type the third person singular form for 'she': ")

        first_plural_present = input("Type the first person plural present form: ")
        second_plural_present = input("Type the first person plural present form: ")
        third_plural_present = input("Type the first person singular present form: ")

        #plural forms
        first_sing_past = input("Type the first person singular past form: ")
        second_sing_past = input("Type the first person singular past form: ")
        third_sing_he_past = input("Type the first person singular past form for 'he': ")
        third_sing_he_past = input("Type the first person singular past form for 'she': ")

        first_plural_past = input("Type the first person plural past form: ")
        second_plural_past = input("Type the first person plural past form: ")
        third_plural_past = input("Type the first person plural past form: ")

        #imperative command forms
        imperative_sing = input("")
        imperative_plural = input("")

        verb_conj = {
        "_id": '"' + root + '"',
        "verbRoot": '"' + root + '"',
        "verbForms":{
        "presentFutureForms": {
            "singularForms": {
                "jiena": '"' + first_sing_present + '"',
                "int": '"' + second_sing_present + '"',
                "hu_huwa": '"' + third_sing_he_present + '"',
                "hi_hija": '"' + third_sing_she_present + '"'
        },
            "pluralForms": {
                "aħna": '"' + first_plural_present + '"',
                "intom": '"' + second_plural_present + '"',
                "huma": '"' + third_plural_present + '"'
            }},
        "pastTenseForms": {
        
            "singularForms": {
                "jiena": '"' + first_sing_past + '"',
                "int": '"' + second_sing_past + '"',
                "hu_huwa": '"' + third_sing_he_past + '"',
                "hi_hija": '"' +  third_sing_she_past + '"'
            },
                "pluralForms": {
                "aħna": '"' + first_plural_past + '"',
                "intom": '"' + second_plural_past + '"',
                "huma": '"' + third_plural_past + '"'
            }}
                "imperativeForms": {
                "singular": '"' + imperative_sing + '"',
                "plural": '"' + imperative_plural + '"'
                } 

            
        }}
        #logic that inserts "null" in an entry if the input entered is blank
        
        #inserts the document and prints the result
        inserted_entry = maltiDB.maltiverb_db.insert_one(verb_conj)
        print(inserted_entry)
