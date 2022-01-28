#!/bin/python3
print("content-type: text/html")
print("Access-Control-Allow-Origin: *\r\n\r\n")
print()


import json
import cgi


abi=json.loads("""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "SchoolID",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "SchoolName",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "TeacherID",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "TecherName",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "SubjectID",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "SubjectName",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "SudentID",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "StudentName",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "StudentPlace",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ClassDate",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "AttendanceFlag",
				"type": "string"
			}
		],
		"name": "recordevent",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getrecords",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "SchoolID",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SchoolName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "TeacherID",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "TecherName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SubjectID",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SubjectName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SudentID",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "StudentName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "StudentPlace",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "ClassDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "AttendanceFlag",
						"type": "string"
					}
				],
				"internalType": "struct StuAtt01.records[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "recordlist",
		"outputs": [
			{
				"internalType": "string",
				"name": "SchoolID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SchoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "TeacherID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "TecherName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SubjectID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SubjectName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SudentID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "StudentName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "StudentPlace",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ClassDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "AttendanceFlag",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "SchoolID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SchoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "TeacherID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "TecherName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SubjectID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SubjectName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SudentID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "StudentName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "StudentPlace",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ClassDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "AttendanceFlag",
				"type": "string"
			}
		],
		"name": "submitrecords",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]
""") 


from web3 import Web3
from web3.middleware import geth_poa_middleware
from flask import Flask, render_template, request
from eth_account import Account
import pprint

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/0719223a9f504c01884bf3c645635282'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0) 
w3.eth.getBlock('latest')

# Get the ETH balance of an address 
w3.eth.getBalance('0x291B0f32E2F25e5F08478c7D9C1B86F7dD4A2C01')

key='b2eebca5e690d08c008a4f95927e55c3f87f0311326e334b6c940478b3514553'
account = w3.toChecksumAddress('0x1335d145A0D27998171d9Fd07B5e98922B8DEdAb')


print(w3.eth.accounts)

address = w3.toChecksumAddress('0xba58c5788c91d8111a71266025cfa1a6603fed33')
deployed_contract = w3.eth.contract(address=address, abi=abi)

SchoolID=cgi.FieldStorage('SchoolID')
SchoolName=cgi.FieldStorage('SchoolName')
TeacherID=cgi.FieldStorage('TeacherID')
TecherName=cgi.FieldStorage('TecherName')
SubjectID=cgi.FieldStorage('SubjectID')
SubjectName=cgi.FieldStorage('SubjectName')
SudentID=cgi.FieldStorage('SudentID')
StudentName=cgi.FieldStorage('StudentName')
StudentPlace=cgi.FieldStorage('StudentPlace')
ClassDate=cgi.FieldStorage('ClassDate')
AttendanceFlag=cgi.FieldStorage('AttendanceFlag')

def submitAttendance(SchoolID,SchoolName,TeacherID,TecherName,SubjectID,SubjectName,SudentID,StudentName,StudentPlace,ClassDate,AttendanceFlag):
	transaction = deployed_contract.functions.submitrecords(SchoolID,SchoolName,TeacherID,TecherName,SubjectID,SubjectName,SudentID,StudentName,StudentPlace,ClassDate,AttendanceFlag).buildTransaction({'from': account})
	transaction.update({ 'nonce' : w3.eth.get_transaction_count(account) })
	signed_tx = w3.eth.account.sign_transaction(transaction, key)
	txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
	print(txn_receipt)
	return True


print(submitAttendance(SchoolID.getvalue('SchoolID'),SchoolName.getvalue('SchoolName'),TeacherID.getvalue('TeacherID'),TecherName.getvalue('TecherName'),SubjectID.getvalue('SubjectID'),SubjectName.getvalue('SubjectName'),SudentID.getvalue('SudentID'),StudentName.getvalue('StudentName'),StudentPlace.getvalue('StudentPlace'),ClassDate.getvalue('ClassDate'),AttendanceFlag.getvalue('AttendanceFlag')))
