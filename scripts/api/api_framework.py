from fastapi import FastAPI
from graphene import ObjectType, Schema

class APIFramework:
    def __init__(self):
        self.app = FastAPI()
        self.schema = Schema(query=ObjectType) 