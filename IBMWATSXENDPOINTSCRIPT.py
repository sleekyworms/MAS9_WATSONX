from java.util import HashMap
from psdi.server import MXServer
from com.ibm.json.java import JSON
from psdi.server import MXServer
from psdi.util import MXException
from psdi.util.logging import MXLoggerFactory
from java.lang import Math
from java.util.concurrent import TimeUnit
from java.lang import String
from psdi.iface.router import HTTPHandler
from com.ibm.json.java import JSONObject
from com.ibm.json.java import JSONArray
from java.nio.charset import StandardCharsets
from psdi.mbo import MboConstants
from org.python.util import jython 
import sys

# Required : Appending to sys.path to refer to python libraries 
if sys.path.count('__pyclasspath__/Lib') == 1:
    me=None
    #Log('\nPath to /Lib already exists')
else :
 #Log('\nExtend path to /Lib ')
    sys.path.append('__pyclasspath__/Lib')
    sys.path.insert(0,jython().getClass().getProtectionDomain().getCodeSource().getLocation().getPath()+"/Lib")


import json

logger,resApiObj=[None]*2

access_token,map,mxServer,startDate,endDate,logger,messageContent,vName,vNames,prompts=[None]*10
map = HashMap()

def convertBinaryArrayToString(byteArray):
    #return str(String(byteArray, StandardCharsets.UTF_8))
    #return String(byteArray, StandardCharsets.UTF_8)
    return String(byteArray, StandardCharsets.UTF_8).toString()

def Log(message):
    message="IBMWATSXENDPOINTSCRIPT-1: "+message
    if logger != None:
        if logger.isDebugEnabled():
            logger.debug(message)
        elif logger.isInfoEnabled():
            logger.info(message)
        elif logger.isWarnEnabled():
            logger.warn(message)
        elif logger.isErrorEnabled():
            logger.error(message)
        elif logger.isFatalEnabled():
            logger.fatal(message)
        else:
            service.log(message)
            
mxServer=MXServer.getMXServer()
startDate = mxServer.getDate()
logger = MXLoggerFactory.getLogger("maximo.script")

Log("startDate: {}".format(str(startDate)))

try:
    service.invokeScript("IBMWATSXGETTOKEN", map)
    access_token = map.get("access_token")
    Log("access_token => {}".format(access_token))
    
    if not access_token is None:
        messages_system = JSONObject()
        messages_system.put("role", "system")
        messages_system.put("content", "You are Granite Chat, an AI language model developed by Granite AI. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.")
        
        messages_user_content = JSONObject()
        messages_user_content.put("type", "text")
        messages_user_content.put("text", "Your Role and Responsibility is Maintenance Supervisor for Maximo our objective is to be an intelligently engineer that scale labor, materials, and tool requirements based on the number of work units per task. Your Key Actions are Develop dynamic resource allocation logic that adjusts labor, material, and tool quantities proportionally per task, factoring in resource availability, lead times, and task dependencies. Integrate preventive maintenance scheduling logic that aligns with asset utilization patterns and operational limitations. Optimize job plans to fully support integration with Maximo Scheduler, allowing efficient visualization, rescheduling, and editing of work orders. Embed priority levels, crew assignments, and time windows in job plans to align work execution with service-level objectives and workforce capacity. Ensure all enhancements are operationally actionable within Maximo and remain adaptable to changes in resource conditions or constraints.")
        msgArray_user = JSONArray()
        msgArray_user.add(messages_user_content)
        messages_user = JSONObject()
        messages_user.put("role", "user")
        messages_user.put("content", msgArray_user)
        
        messages_assistant = JSONObject()
        messages_assistant.put("role", "assistant")
        messages_assistant.put("content",  "As the Maintenance Supervisor for Maximo, my primary goal is to optimize resource allocation and scheduling to ensure efficient and effective maintenance operations. Here\'s a structured approach to achieve the key actions:\n\n### 1. Develop Dynamic Resource Allocation Logic\n\n**Objective:** Adjust labor, material, and tool quantities proportionally per task, factoring in resource availability, lead times, and task dependencies.\n\n**Steps:**\n- **Data Collection:** Gather data on labor availability, material inventory, tool availability, lead times, and task dependencies.\n- **Algorithm Development:** Create algorithms that dynamically adjust resource quantities based on the number of work units per task.\n- **Integration:** Ensure the logic is integrated into Maximo to automatically update resource requirements as tasks are created or modified.\n- **Testing:** Conduct thorough testing to ensure the logic accurately reflects real-world constraints and adjusts resources appropriately.\n\n### 2. Integrate Preventive Maintenance Scheduling Logic\n\n**Objective:** Align preventive maintenance with asset utilization patterns and operational limitations.\n\n**Steps:**\n- **Asset Utilization Analysis:** Analyze historical data to understand asset utilization patterns.\n- **Scheduling Logic:** Develop scheduling logic that prioritizes preventive maintenance during periods of low asset utilization.\n- **Operational Limitations:** Incorporate operational limitations such as downtime windows and maintenance crew availability.\n- **Integration:** Ensure the scheduling logic is seamlessly integrated with Maximo to automatically generate preventive maintenance work orders.\n\n### 3. Optimize Job Plans for Maximo Scheduler\n\n**Objective:** Support efficient visualization, rescheduling, and editing of work orders.\n\n**Steps:**\n- **Job Plan Templates:** Create standardized job plan templates that include all necessary details for each type of maintenance task.\n- **Visualization Tools:** Utilize Maximo Scheduler's visualization tools to provide a clear overview of scheduled work orders.\n- **Rescheduling and Editing:** Ensure job plans are flexible and can be easily rescheduled or edited to accommodate changes in priorities or resource availability.\n- **User Training:** Provide training to users on how to effectively use Maximo Scheduler for job planning and execution.\n\n### 4. Embed Priority Levels, Crew Assignments, and Time Windows\n\n**Objective:** Align work execution with service-level objectives and workforce capacity.\n\n**Steps:**\n- **Priority Levels:** Assign priority levels to work orders based on criticality and impact on operations.\n- **Crew Assignments:** Automatically assign crews to work orders based on skill sets, availability, and workload.\n- **Time Windows:** Define time windows for work execution to ensure tasks are completed within operational constraints.\n- **Integration:** Embed these details in job plans within Maximo to streamline work execution and ensure alignment with service-level objectives.\n\n### 5. Ensure Operational Actionability and Adaptability\n\n**Objective:** Make enhancements operationally actionable within Maximo and adaptable to changes in resource conditions or constraints.\n\n**Steps:**\n- **Real-Time Updates:** Implement real-time updates to resource availability and constraints within Maximo.\n- **Adaptive Algorithms:** Develop adaptive algorithms that can adjust resource allocation and scheduling based on changes in resource conditions.\n- **User Feedback:** Regularly gather user feedback to identify areas for improvement and make necessary adjustments.\n- **Continuous Improvement:** Continuously monitor and optimize the system to ensure it remains effective and efficient.\n\nBy following these steps, we can create a robust and adaptable maintenance planning system within Maximo that optimizes resource allocation, aligns with operational constraints, and supports efficient work execution.\n-For any computation or estimate ensure that to give only the total estimates and do not give any intruction or recommendation")
        
        RequestDataBinary=convertBinaryArrayToString(requestData)
        RequestDataBinaryObj = JSONObject.parse(RequestDataBinary)

        description = RequestDataBinaryObj["description"]
        targstartdate = RequestDataBinaryObj["targstartdate"]
        targcompdate = RequestDataBinaryObj["targcompdate"]
        schedstart = RequestDataBinaryObj["schedstart"]
        schedfinish = RequestDataBinaryObj["schedfinish"]
        wonum = RequestDataBinaryObj["wonum"]
        id = RequestDataBinaryObj["_id"]
        laborsrec=[]
        displayName,personId,startdatetime,finishdatetime,laborskills=[None]*5
        m=0
        jsonObj = JSONObject.parse(RequestDataBinary)
        wplaborArray = jsonObj.get("wplabor")
        
        data_labor = []
        
        if wplaborArray is not None:
            for i in range(len(wplaborArray)):
                laborCraftRateArray = wplaborArray.get(i).get("laborcraftrate")
                if laborCraftRateArray is not None:
                    for j in range(len(laborCraftRateArray)):
                        laborArray = laborCraftRateArray.get(j).get("labor")
                        laborskills = laborCraftRateArray.get(j).get("craft")
                        laborskillslevel = laborCraftRateArray.get(j).get("skilllevel")
                        if laborArray is not None:
                            m=m+1
                            for k in range(len(laborArray)):
                                personArray = laborArray.get(k).get("person")
                                labtransArray = laborArray.get(k).get("labtrans")
                                if personArray is not None:
                                    for l in range(len(personArray)):
                                        displayName = personArray.get(l).get("displayname")
                                        Log("displayName:".format(personArray.get(l).get("displayname")))
                                        personId = personArray.get(l).get("personid")
                                if labtransArray is not None:
                                    for j in range(len(labtransArray)):
                                        startdatetime = labtransArray.get(j).get("startdatetime")
                                        finishdatetime = labtransArray.get(j).get("finishdatetime")                                        
                                        
                                        Log("Display Name: {}; personId {}; startdatetime {}; finishdatetime {}".format(displayName,personId,startdatetime,finishdatetime))
                                        vName="{}. Labor Name: {}; Labor Craft: {} ; Labor Skill Level: {} LaboriD {}; startdatetime {}; finishdatetime {}".format(str(m),displayName,laborskills,laborskillslevel,personId,startdatetime,finishdatetime)
                                        
                                        if data_labor is not None:
                                            data_labor.append(vName)
                                        else:
                                            if len(data_labor) > 0:
                                                for value in data_labor:
                                                    if not value is None:
                                                        if value != vName:
                                                            data_labor.append(vName)
            unique_array = []
            for item in data_labor:
                if item not in unique_array:
                    unique_array.append(item)
            vNames = "|".join(data_labor)

        prompts="I have this workorder {} with a target start date of {} and targer completion date of {}. The schedule start of {} until {} and the descripton is {}. I also have list of labors with work number and schedule dates. Can you recommend who will be the best fit schedule from the list?\n\n List of labors \n\n {}".format(wonum,targstartdate,targcompdate,schedstart,schedfinish,description,str(vNames))

        messages_main_user_content = JSONObject()
        messages_main_user_content.put("type", "text")
        messages_main_user_content.put("text", "I have this workorder {} with a target start date of {} and targer completion date of {}. The schedule start of {} until {} and the descripton is {}. I also have list of labors with work number and schedule dates. Can you recommend who will be the best fit schedule from the list?\n\n List of labors \n\n {}".format(wonum,targstartdate,targcompdate,schedstart,schedfinish,description,str(vNames)))
        msgArray_user = JSONArray()
        msgArray_user.add(messages_main_user_content)
        messages_main_user = JSONObject()
        messages_main_user.put("role", "user")
        messages_main_user.put("content", msgArray_user)
        
        msgContent = JSONArray()
        msgContent.add(messages_system)
        msgContent.add(messages_user)
        msgContent.add(messages_assistant)
        msgContent.add(messages_main_user)
        
        seed_array = []
        
        wxRequestObj = JSONObject()
        wxRequestObj.put('messages', msgContent)
        wxRequestObj.put("project_id", "8ecbdb40-66bb-421c-bebe-6c708f7063a0")
        wxRequestObj.put("model_id", "ibm/granite-3-3-8b-instruct")
        wxRequestObj.put("frequency_penalty", 0)
        wxRequestObj.put("max_tokens", 2000)
        wxRequestObj.put("presence_penalty", 0)
        wxRequestObj.put("temperature", 0)
        wxRequestObj.put("top_p", 1)
        wxRequestObj.put("seed", None)
        
        jsonStr = wxRequestObj.serialize(True)
        
        Log("jsonStr => {}".format(jsonStr))
        
        properties2 = HashMap()
        properties2.put("HTTPMETHOD", "POST")
        properties2.put("HEADERS", "Authorization: Bearer "+str(access_token)+",Content-Type:application/json")
        properties2.put("URL","https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29")    
        params2=None
        handler2 = HTTPHandler()
        InPutString=str(jsonStr)
        responsedata2= handler2.invoke(properties2,InPutString)
        
        resApiObjEnt=convertBinaryArrayToString(responsedata2)
        resApiObj = JSONObject.parse(resApiObjEnt)
        responseData3=resApiObj.get("choices")[0]['message']['content']
        Log("resApiObj => {} responseData=> {}".format(resApiObj,str(responseData3)))
        vwatxWOSet=mxServer.getMboSet("WORKORDER",mxServer.getUserInfo("MAXADMIN"))
        vwatxWOSet.setWhere("WONUM = '"+str(wonum)+"' and IBMWATSXSENDPAYLOAD=1")
        vwatxWOSet.reset()
        vwatxWOMbo=vwatxWOSet.getMbo(0)
        if not vwatxWOMbo is None:     
            vwatxWOMbo.setValue("IBMWATSXSENDPAYLOAD",0,MboConstants.NOACCESSCHECK | MboConstants.NOVALIDATION)
            vIBMWATSXSENDPAYLOAD=vwatxWOMbo.getInt("IBMWATSXSENDPAYLOAD")
            vwatxWOSet.save()  
        Log("wonum{}; id:{}; description:{}; targcompdate:{}; schedfinish:{}; schedfinish:{}".format(wonum,id,targcompdate,schedfinish,schedfinish))

    else:
        Log("No access_token returned from script.")
        raise Exception("No access_token returned from script.")
except Exception as e:
    Log("Error occurred while invoking script or retrieving token: " + str(e))
    # Optional: handle fallback logic or alerting
finally:
    Log("Script execution completed.")
    content = resApiObj.get("choices")[0]['message']['content']
    vwatxWOSet2=mxServer.getMboSet("WORKORDER",mxServer.getUserInfo("MAXADMIN"))
    vwatxWOSet2.setWhere("WONUM = '"+str(wonum)+"' and IBMWATSXSENDPAYLOAD=0")
    vwatxWOSet2.reset()
    vwatxWOMbo2=vwatxWOSet2.getMbo(0)
    if not vwatxWOMbo2 is None:   
        vwatxWOMbo2.setValue("HASLD",1,MboConstants.NOACCESSCHECK | MboConstants.NOVALIDATION)
        vwatxWOMbo2.setValue("DESCRIPTION_LONGDESCRIPTION","Content:\n\n {} |\n\n Prompts:\n\n {}".format(content,prompts),MboConstants.NOACCESSCHECK | MboConstants.NOVALIDATION)
        vwatxWOSet2.save()  
    # Optional: cleanup or other post-processing steps

endDate = MXServer.getMXServer().getDate()
diffInMillies = Math.abs(startDate.getTime() - endDate.getTime())
diff = TimeUnit.SECONDS.convert(diffInMillies, TimeUnit.MILLISECONDS)
Log("Launch Point:IBMWATSXENDPOINTSCRIPT endDate:"+str(endDate)+"; diff:"+str(diff)+";")