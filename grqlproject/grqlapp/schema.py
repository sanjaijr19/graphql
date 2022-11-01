import graphene
from graphene_django import DjangoObjectType
from .models import Bio



class BioType(DjangoObjectType):
    class Meta:
        model=Bio
        fields=("id","name","age","native")


class Query(graphene.ObjectType):
    all_bio = graphene.List(BioType)

    def resolve_all_bio(root, info):
        return Bio.objects.all()


class BioMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name=graphene.String(required=True)
        age=graphene.Int(required=True)
        native=graphene.String(required=True)
    bio=graphene.Field(BioType)

    @classmethod
    def mutate(cls,root,info,id,name,age,native):
        bio=Bio.objects.get(id=id)
        # bio=Bio(name=name,age=age,native=native)
        bio.name=name
        bio.age=age
        bio.native=native
        bio.delete()
        return BioMutation(bio=bio)
class Mutation(graphene.ObjectType):
    update_bio=BioMutation.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)
