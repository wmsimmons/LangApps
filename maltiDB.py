#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pymongo
from pymongo import MongoClient

# coding= utf8


#connect to pymongo
client = MongoClient("localhost", 27017)
db = client.maltiVerbConjugator

verbs = []

#connection = MongoClient
#connection = MongoClient()
#db = connection.maltiVerbConjugator

# #asks for which verb, tense and subject you want
# verb_selector = input("Insert desired verb")
# verb_tense_selector = input("Insert which tense")
# desired_pronoun = input("Insert which subject you want")

def connect_maltidb():
    """connects to the maltiVerbConjugator database"""
    connection = MongoClient
    connection = MongoClient()
    db = connection.maltiVerbConjugator
    maltiverb_db = db.maltiVerbConjugator
    return maltiverb_db


#attach the maltiVerbConjugator database to the content of verbs verb_selector
#logic for whether tense is past or present past on user raw_input verb_tense_selector
#logic to retrieve the correct verb on user raw_input verb_selector

#log to choose the subject based on user raw_input
#when user raw_inputs verb, tense and pronoun, look up in database 
#and return the result of the 3 raw_inputted values



#how to structure mongo collection to work with verb tenses,
#pronouns and verb roots


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
    third_sing_she_past = input("Type the first person singular past form for 'she': ")

    first_plural_past = input("Type the first person plural past form: ")
    second_plural_past = input("Type the first person plural past form: ")
    third_plural_past = input("Type the first person plural past form: ")

    #imperative command forms
    imperative_sing = input("Type the imperative singular form: ")
    imperative_plural = input("Type the imperative plural form: ")
    
    #how to structure mongo collection to work with verb tenses,
    #pronouns and verb roots
    verb_conj = {
    "_id":  root, 
    "verbRoot": root,
    "verbForms":{
    "presentFutureForms": {
        "singularForms": {
            "jiena":  first_sing_present,
            "int": second_sing_present,
            "hu_huwa":  third_sing_he_present,
            "hi_hija":  third_sing_she_present 
    },
        "pluralForms": {
            "aħna": first_plural_present,
            "intom": second_plural_present,
            "huma": third_plural_present
        }},
    "pastTenseForms": {
    
        "singularForms": {
            "jiena": first_sing_past,
            "int": second_sing_past,
            "hu_huwa": third_sing_he_past,
            "hi_hija": third_sing_she_past 
        },
            "pluralForms": {
            "aħna": first_plural_past,
            "intom": second_plural_past,
            "huma": third_plural_past
        }},
    "imperativeForms": {
            "singular": imperative_sing,
            "plural": imperative_plural 
            } 
           }};

    #logic that inserts "null" in an entry if the input entered is blank
    
    print(verb_conj)
    confirmation = input("Are you sure this verb" + ' + root + ' +  "is conjugated correctly? Write 'yes' or 'y' to confirm. ")
    if confirmation == 'yes' or 'y':
        #inserts the document and prints the result
        maltidb = connect_maltidb()
        inserted_entry = maltidb.insert_one(verb_conj)
        return inserted_entry
    elif confirmation == 'n' or 'no':
        pass
    
def verb_delete(root):
    maltidb = connect_maltidb()
    entry = maltidb.find({"_id": root})
    for rootform in entry:
        print(rootform)

    confirmation = input("Are you sure that you want to delete this document? Type 'yes' or 'no' to confirm: ")
    if confirmation == 'yes' or 'y':
        #removes entry from db and returns what was deleted
        deleted_entry = maltidb.remove(rootform)
        return deleted_entry
    elif confirmation == 'no' or 'n':
        pass