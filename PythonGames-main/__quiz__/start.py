from ui import Console
from controller import Service
from repo import Repository
from validation import Validator

repository = Repository()
validator = Validator()
service = Service(repository,validator)
console = Console(service)
console.run()