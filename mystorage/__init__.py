import os,json,shutil

class Colors: fail = '\033[91m' ; good = '\033[92m' ; end = '\033[0m'
# TODO: work on Tables()
class Tables:
    def __init__(self,tableName:str):
        self.__thisDir = os.path.dirname(__file__)+'/tables/'
        self.__tableName = tableName.strip()
        self.__tableDir = self.__thisDir+self.__tableName+'/'
        self.__tableStructurePath = self.__thisDir+self.__tableName+'/__init__.json'
        self.__table = True
        # create tables folder if not exists
        if not os.path.isdir(self.__thisDir): os.mkdir(self.__thisDir)
        # check if table exists
        if not os.path.isdir(self.__tableDir): self.__table = False

    def createTable(self,tableStructure:dict):
        # check if table already exists
        if not self.__table: return {'status':False,'msg':f'Table {self.__tableName} already exists'}
        # else try to create a new one
        acceptedRowTypes = ['str','list','dict','int','float']
        for rowName,rowType in tableStructure.items():
            if rowType not in acceptedRowTypes:
                print(f'{Colors.fail}Wrong table row type {rowType} use python data types {acceptedRowTypes}{Colors.end}')
                return {'status':False,'msg':f'Wrong table row type {rowType}'}
        #create table directory
        os.mkdir(self.__tableDir)
        # create table structure (json init file)
        open(self.__tableStructurePath,'w').write(json.dumps(tableStructure))
        return {'status':True,'msg':f'Table {self.__tableName} was created'}

    def tableStructure(self,updateStructure=False,addStructure=False):
        # check if tables exists, if not return false status
        if not self.__table: return {'status':False,'msg':f'Table {self.__tableName} do not exists please use .createTable() to create a new one'}
        #----
        removeAtTheEnd,addAtTheEnd = [],[]
        acceptedRowTypes = ['str','list','dict','int','float']
        tableStructure = json.loads(open(self.__tableStructurePath,'r').read())
        # if add structure is true
        if addStructure:
            addingStructure = True
            while addingStructure:
                newStructureInput = input('Add new table structure use this format using double quotes {"rowName":"rowDataType"}   or keep empty to skip:  ').strip()
                if not newStructureInput: addingStructure = False ; continue
                try:
                    newStructure = json.loads(newStructureInput)
                    _name,_type = list(newStructure)[0],newStructure[list(newStructure)[0]]
                    # if row type not accepted
                    if _type not in acceptedRowTypes:
                        return {'status':False,'msg':f'Wrong data type >>{_type}<< use python data types: {acceptedRowTypes}'}
                    # if this row name already exists 
                    if _name in tableStructure:
                        print(f'{Colors.fail}Structure {_name} already in this table structure{Colors.end}') ; continue
                    # if everything passed add to table structure
                    tableStructure[_name]=_type
                except: return {'status':False,'msg':'Error adding structure make sure to use double quotes example: {"rowName":"rowDataType"}'}
        # if update structure is true
        if updateStructure:
            for rowName,rowType in tableStructure.items():
                updateInput = input('Update {'+'"'+rowName+'":"'+rowType+'"'+'} use this format using double quotes {"rowName":"rowDataType"}   or keep empty to skip:  ').strip()
                if updateInput == '': continue
                try:
                    thisRowChanges = json.loads(updateInput)
                    _name,_type = list(thisRowChanges)[0],thisRowChanges[list(thisRowChanges)[0]]
                    # if row type not accepted
                    if _type not in acceptedRowTypes:
                        return {'status':False,'msg':f'Wrong data type >>{_type}<< use python data types: {acceptedRowTypes}'}
                    # if this row change key name add it to remove at the end list because dict can not change size or name when looping
                    # else if it is the same name change the key value (type)
                    if _name != rowName:
                        removeAtTheEnd.append(rowName)
                        addAtTheEnd.append({'name':_name,'type':_type})
                    elif _name == rowName: tableStructure[rowName] = _type
                except: return {'status':False,'msg':'Error make sure to use double quotes example: {"rowName":"rowDataType"}'}
        # if everything passed make changes and updated all object in this table
        for name in removeAtTheEnd: del tableStructure[name]
        for _dict in addAtTheEnd: tableStructure[_dict['name']] = _dict['type']
        # save changes
        open(self.__tableStructurePath,'w').write(json.dumps(tableStructure))
        return tableStructure

    def reset(self):
        # check if tables exists, if not return false status
        if not self.__table: return {'status':False,'msg':f'Table {self.__tableName} do not exists please use .createTable() to create a new one'}
        #----
        answer = input('This will delete all table in the tables directory ok/no?  ').strip().lower()
        if answer == 'ok' or answer == 'yes':
            for table in os.listdir(self.__thisDir):
                shutil.rmtree(self.__thisDir+table)     
            return {'status':True,'msg':'All tables were deleted'}

# TODO: work on Collections()
class Collections:
    def __init__(self,collectionName:str,defaultData='list'):
        self.__thisDir = os.path.dirname(__file__)+'/collections/'
        self.collectionName = collectionName
        self.collectionPath = self.__thisDir+self.collectionName+'.json'
        # create collections folder if not exists
        if not os.path.isdir(self.__thisDir): os.mkdir(self.__thisDir)
        # if collection json file do not exists make one
        if not os.path.exists(self.collectionPath):
            if defaultData == 'list': open(self.collectionPath,'w').write('[]')
            else: open(self.collectionPath,'w').write('{}')

    def add(self,data:dict):
        collectionData = json.loads(open(self.collectionPath,'r').read())
        try:
            for dataKey,dataValue in data.items(): collectionData[dataKey]=dataValue
        except: return {'status':False,'msg':f'Error inserting data into collection data'}
        open(self.collectionPath,'w').write(json.dumps(collectionData,indent=4))
        return {'status':True,'msg':f'Data inserted into collection data'}

    def delete(self,keyName:str):
        collectionData = json.loads(open(self.collectionPath,'r').read())
        if keyName in collectionData:
            del collectionData[keyName]
            open(self.collectionPath,'w').write(json.dumps(collectionData,indent=4))
            return {'status':True,'msg':f'{keyName} deleted'}
        return {'status':False,'msg':f'{keyName} not in collection data'}

    def find(self,keyName:str):
        collectionData = json.loads(open(self.collectionPath,'r').read())
        if keyName in collectionData: return collectionData[keyName]
        return {'status':False,'msg':f'{keyName} not in collection data'}

    def read(self):
        collectionData = json.loads(open(self.collectionPath,'r').read())
        return collectionData

    def update(self,newData):
        try: open(self.collectionPath,'w').write(json.dumps(newData,indent=4)) ; return True
        except: return False

    def drop(self): 
        if os.path.exists(self.collectionPath): os.remove(self.collectionPath)

    def reset(self): 
        # this will delete all collections from collections directory
        answer = input('All collections will be deleted ok/no?').strip().lower()
        if answer == 'ok' or answer == 'yes':
            for collection in os.listdir(self.__thisDir): os.remove(self.__thisDir+collection)
            return {'status':True,'msg':f'All collections were deleted'}

class JsonObjects:
    def __init__(self,fileName:str,defaultData='list'):
        self.thisDir = os.path.dirname(__file__)+'/json/'
        self.fileName = fileName
        self.jsonPath = f'{self.thisDir+fileName}.json'
        self.jsonData = False
        # create json folder if not exists
        if not os.path.isdir(self.thisDir): os.mkdir(self.thisDir)
        # create this json file if not exists
        if not os.path.exists(self.jsonPath):
            if defaultData == 'list': open(self.jsonPath,'w').write('[]')
            else: open(self.jsonPath,'w').write('{}')

    def read(self):
        if os.path.exists(self.jsonPath):
            jsonData = json.loads(open(self.jsonPath,'r').read())
            self.jsonData = jsonData ; return jsonData
        else: print(f'{Colors.fail} The json object {self.fileName} do not exists{Colors.end}') ; return False

    def drop(self):
        if os.path.exists(self.jsonPath): os.remove(self.jsonPath) ; return True
        else: print(f'{Colors.fail} The json object {self.fileName} do not exists{Colors.end}') ; return False

    def update(self):
        if self.jsonData: open(self.jsonPath,'w').write(json.dumps(self.jsonData,indent=4)) ; return True
        else: print(f'{Colors.fail} Use .read() to read the json data before you can update it.{Colors.end}') ; return False

    def reset(self): 
        # this will delete all json objects
        answer = input('All the json objects will be deleted ok/no?').strip().lower()
        if answer == 'ok' or answer == 'yes':
            for obj in os.listdir(self.thisDir): os.remove(self.thisDir+obj)
        return True


# table = Tables('test')

# collection = Collections('test')

# jsonObject  = JsonObjects('stockSymbols',defaultData='list')
# symbols = jsonObject.read()
# print(symbols)

# TODO: work on tables()
# TODO: work on collection() 