import graphene
from student.schema import Query as student_query

# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")




class Query(student_query):
    pass

schema=graphene.Schema(query=Query)