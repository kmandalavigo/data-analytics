import json
def searchTestAndValue(row, testData):
    testValue = testData['value']
    testName = testData['name']
    isFasting = testData['fasting']
    actualtestValue = row.result_idw_result_value.isdigit() and int(row.result_idw_result_value)
    testEvalString = testValue.format(actualtestValue)
    isFastingMatch =  row.accession_idw_fasting_ind == 'Y' if isFasting else True
    testValueMatch = actualtestValue and eval(testEvalString) and isFastingMatch
    actualTestName = row.result_idw_result_name
    return ((testName in actualTestName) and testValueMatch)

def searchRecords(row, testData):
    testValue = testData['value']
    testName = testData['name']
    isFasting = testData['fasting']
    actualtestValue = row.result_idw_result_value.isdigit() and int(row.result_idw_result_value)
    testEvalString = testValue.format(actualtestValue)
    isFastingMatch =  row.accession_idw_fasting_ind == 'Y' if isFasting else True
    testValueMatch = actualtestValue and eval(testEvalString) and isFastingMatch
    actualTestName = row.result_idw_result_name
    ({name} == 'h1bc' and {value}> 100)
    return ((testName in actualTestName) and testValueMatch)


def searchPatientByDemoGraphics(row, patientDat):
    testAge = patientDat['age']
    testGender = patientDat['gender']
    ageInYears = int(row.age_in_years) if row.age_in_years.isdigit() else 0 
    ageEvalString = testAge.format(ageInYears)
    genderEvalString = testGender.format(row.pm_gender)
    return eval(ageEvalString) and eval(genderEvalString)

criteria = {
    'test':{
     'name': 'LDL-C',
     'value': '{0} > 100 and {0} < 190',
     'fasting': True
  },
    'demographics': {
        'age':' {0} > 40',
        'gender':'\'{0}\' == \'M\''
    }    
}


def handleResource(op):
    # print('({0} {1})'.format(op['resource']['code']['coding'][0]['code'], op['resource']['expression']))
    print('({0} {1})'.format(op['resource']['code']['text'], op['resource']['expression']))

def handleAllOperators(operators):
    for op in operators :
        if('resource') in op:
            print('and')
            handleResource(op)

        if('any') in op:
            print('and')
            handleAnyOperators(op['any'])

        if('and') in op:
            print('and')
            handleAllOperators(op['and'])            
        
def handleAnyOperators(operators):
    for op in operators :
        if('resource') in op:
            print('or')
            handleResource(op)

        if('any') in op:
            print('or')
            handleAnyOperators(op['any'])

        if('all') in op:
            print('or')
            handleAllOperators(op['and'])        


with open("test.json") as json_file:
    json_data = json.load(json_file)
    allOpertors = json_data['all']
    handleAllOperators(allOpertors)