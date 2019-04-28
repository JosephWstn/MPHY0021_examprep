from argparse import ArgumentParser
import yaml
from .laboratory import Laboratory


def abracadabra():
    parser = ArgumentParser(description="Runs experiment")

    #two arguments, the yaml file of the shelves and the reactions tag
    parser.add_argument('--reactions', action="store_true")
    parser.add_argument('yaml_file')
    arguments = parser.parse_args()

    #open the yaml file and separate into two shelves
    shelves_dictionary = yaml.load(open(arguments.yaml_file))
    shelf1 = shelves_dictionary["lower"]
    shelf2 = shelves_dictionary["upper"]

    #create laboratory object and run experiment
    lab = Laboratory(shelf1, shelf2)
    lab.run_full_experiment(arguments.reactions)

if __name__== "__main__":
    abracadabra()