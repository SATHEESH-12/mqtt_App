from ast import Not
import paho.mqtt.client as mqtt
import json
import re

class connectSandesh:

    def __init__(self) -> None:
        try:
            self.__mqttClient=mqtt.Client("dummy")
        except exception as ex:
            print(ex)

        

    async def ConnectMessanger(self,connReq : str) -> str:
        try:
            if connReq is None or connReq=="":
                return json.dumps(ConnRes("Requet Cannot be null",0,False).__dict__)

            reqData=json.loads(connReq.__dict__)
            self.__mqttClient.username_pw_set("dummy","OPENID~keycloakAuth"+reqData.token+"~")
            self.__mqttClient.clean_session=True
            self.__mqttClient.protocol=mqtt.MQTTv311

            await self.__mqttClient.connect()
            self.__mqttClient.loop_start()
            return json.dumps(ConnRes("Connected successfully", 1, True).__dict__)

            self.__mqttClient.connect()
        except Exception as ex:
            print(ex)
    

    def SubscribeFeed(subReq : str) -> str:
        try:
            if subReq is None or subReq=="":
                return json.dumps(SubRes("Requet Cannot be null",[]).__dict__)

            resData=SubRes()
            reqData=json.loads(subReq.__dict__)
            pattern = r'^[0-9a-z/]+$'
            topics=[]
            for topic in reqData.topiclist:
                if (re.fullmatch()(pattern,topic)):
                    topics.append((topic,mqtt.SubscribeOptions(qos=0)))
                else:
                    resData.topicRes.append("Invalid topic",topic)







        except Exception as ex:
            print(ex)


class ConnReq:

    def __init__(self,host:str,port:int,token:str):
        self.host=host
        self.port=port
        self.token=token

class ConnRes:
    def __init__(self,resultCode:str,maxQos:int,retainAvailable:bool):
        self.resultCode=resultCode
        self.maxQos=maxQos
        self.retainAvailable=retainAvailable

class SubReq:
    def  __init__(self,feedType : str,topicList :list):
        self.topicList=topicList
        self.feedType=feedType

class SubRes:
    def  __init__(self,result : str,topicRes : list):
        self.topicRes=topicRes
        self.result=result

class TopicResult:
    def  __init__(self,resultcode : str,topic :str):
        self.resultcode=resultcode
        self.topic=topic

       
    