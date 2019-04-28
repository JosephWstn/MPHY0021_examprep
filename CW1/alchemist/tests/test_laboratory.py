from pytest import raises
import yaml
from ..laboratory import Laboratory
import os

#read the yaml file with the shelves for testing
with open(os.path.join(os.path.dirname(__file__),
                       'fixtures.yml')) as fixtures_file:
    yaml_file = yaml.load(fixtures_file)


test_data = yaml_file["standard_shelves"]

#negative test to see that a TypeError is raised when there are three
# shelves given
def test_number_of_shelves():
    """
    Tests that a TypeError is raised if the three shelves are given
    """
    shelf1 = test_data['lower']
    shelf2 = test_data['upper']
    with raises(TypeError) as exception:
        lab = Laboratory(shelf1, shelf2, shelf2)
        lab.run_full_experiment(reactions= False)


#test the error if a number is in the shelves
def test_shelf_strings():
    """
    Tests a TypeError is raised if the shelves aren't all strings
    """
    shelf1 = test_data['lower']
    shelf2 = ["X",2,"antiX"]
    with raises(TypeError) as exception:
        lab=Laboratory(shelf1, shelf2)
        lab.run_full_experiment(reactions=False)


#Test the full experiment method works
def test_run_full_experiment():
    """
    Tests that the output is as expected when full experiment is run
    """
    shelf1 = test_data['lower']
    shelf2 = test_data['upper']
    expected_results = yaml_file["answer"]
    lab = Laboratory(shelf1, shelf2)
    assert(lab.run_full_experiment(reactions=False) == expected_results)


def test_can_react():
    """
    Test the method can_react
    """
    sub_1 = "A"
    sub_2 = "antiA"
    #make an empty laboratory object since it's not needed
    lab = Laboratory([], [])
    assert(lab.can_react(sub_1, sub_2) == True)

def test_update_shelves():
    """
    Test the method update_shelves
    """
    shelves = yaml_file["update_shelves"]
    shelf1 = shelves["lower"]
    shelf2 = shelves["upper"]
    expected = yaml_file["update_result"]["lower"],\
               yaml_file["update_result"]["upper"]
    lab = Laboratory(shelf1, shelf2)
    assert(lab.update_shelves("antiA", 0)== expected)

def test_do_a_reaction():
    """
    Test the do_a_reaction method
    """
    shelves = yaml_file["update_shelves"]
    shelf1 = shelves["lower"]
    shelf2 = shelves["upper"]
    expected = yaml_file["update_result"]["lower"],\
               yaml_file["update_result"]["upper"]
    lab = Laboratory(shelf1, shelf2)
    assert(lab.do_a_reaction() == expected)

#test that experiment runs with an empty shelf
def test_one_empty_shelf():
    """
    Tests the output is as expected when one shelf is empty
    """
    shelf1 = test_data['lower']
    shelf2 = []
    #since one shelf is empty, nothing should change on the shelves
    expected_results = {'upper' : shelf2, 'lower' : shelf1}
    lab=Laboratory(shelf1, shelf2)
    assert(lab.run_full_experiment(reactions=False) == expected_results)

#test that experiment runs with two empty shelves
def test_two_empty_shelves():
    """
    Tests the output is as expected when both shelves are empty
    """
    shelf1 = []
    shelf2 = []
    #sincee both shelves are empty, nothing should change
    expected_results = {'upper' : shelf2, 'lower' : shelf1}
    lab=Laboratory(shelf1, shelf2)
    assert(lab.run_full_experiment(reactions= False) == expected_results)

#test that if there are multiple copies of the same potion, it will pick
# one of the possible reactions
def test_multiple_options():
    """
    Test that the experiment works when there are repeats of reactable
    substances
    """
    multiple_selection = yaml_file["multiple_selection_shelves"]
    shelf1 = multiple_selection['lower']
    shelf2 = multiple_selection['upper']
    lab = Laboratory(shelf1, shelf2)
    results = lab.run_full_experiment(reactions= False)
    worked = False
    for i in ("1", "2", "3"):
        expected = yaml_file["results_"+i]
        if results == expected:
            worked = True
    assert(worked == True)

#test that outputting number of reactions works
def test_reactions_tag():
    """
    Tests the output is as expected when the reactions tag is used
    """
    shelf1 = test_data['lower']
    shelf2 = test_data['upper']
    lab = Laboratory(shelf1, shelf2)
    assert(lab.run_full_experiment(reactions=True) == 2)

#test that if there are multiple copies of the same potion, it will pick
#one of the possible reactions at random
def test_random_selection():
    """
    Tests that the selection is random when there are repeats of reactable
    substances
    """
    results = []
    random_selection = yaml_file["random_selection_shelves"]
    shelf1 = random_selection['lower']
    shelf2 = random_selection['upper']
    #loop the reaction 30 times, it is likely both possible selections will
    #occur if the selection is random
    for y in range(30):
        lab = Laboratory(shelf1, shelf2)
        results_current = lab.run_full_experiment(reactions= False)
        results.append(results_current)
    result_four = yaml_file["results_4"]
    result_five = yaml_file["results_5"]
    assert(result_four in results and result_five in results)