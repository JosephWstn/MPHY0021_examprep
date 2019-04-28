import random


class Laboratory:
    def __init__(self, shelf1, shelf2):
        """ Constructor for class Laboratory

        Parameters
        ----------
        shelf1: list
            The substances on the lower shelf
        shelf2: list
            The substances on the upper shelf
        """
        self = self
        self.shelf1 = shelf1
        self.shelf2 = shelf2

    def can_react(self, substance1, substance2):
        """ Tests whether two substances can react

        Parameters
        ----------
        substance1: str
            The name of the first substance being tested
        substance2: str
            The name of the second substance being tested

        Returns:
        bool
            True if the two can react, false if they cannot
        """

        return (substance1 == "anti" + substance2) or (substance2 == "anti" +
                                                       substance1)

    def update_shelves(self, substance1, substance2_index):
        """ Remove the substances from the shelves that are going to be
            reacted

        Parameters
        ----------
        substance1: str
            The name of the substance on shelf1
        substance2_index: int
            The position of the opposite substance on shelf2

        Returns
        -------
        lists
            the updates shelf1 and shelf2 after the reaction
        """

        index1 = self.shelf1.index(substance1)
        # Updates the shelves as two substances are used in the reaction
        self.shelf1 = self.shelf1[:index1] + self.shelf1[index1+1:]
        self.shelf2 = self.shelf2[:substance2_index]\
            + self.shelf2[substance2_index+1:]
        return self.shelf1, self.shelf2

    def do_a_reaction(self):
        """ Generates a reaction.Goes through substances in shelf1 and makes
                  it react with a suitable shelf2 substance

        Returns
        -------
        lists
            the updated shelves after a reaction has taken place
        """
        for substance1 in self.shelf1:
            # finds the possible targets in shelf2
            possible_targets = [i for i, target in enumerate(self.shelf2) if
                                self.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                # carries out reaction after choosing one of the possible
                # targets at random
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(substance1, substance2_index)
        return self.shelf1, self.shelf2

    def run_full_experiment(self, reactions):
        """ Runs all possible reactions, prints how many happened, and returns
                  final state of shelves

        Parameters
        ----------
        reactions: bool
            If true, return just the number of reactions that happened

        Returns
        -------
        lists
            the updates shelves after all of the reactions

        """
        count = 0
        ended = False
        # loop reactions until all possible reactions have been done
        while not ended:
            # update the shelves each loop
            shelf1_new = self.shelf1
            shelf2_new = self.shelf2
            self.do_a_reaction()
            # update reaction counter
            if shelf1_new != self.shelf1:
                count += 1
            ended = (shelf1_new == self.shelf1) and (shelf2_new == self.shelf2)
        # if reactions tag is used, just return number of reactions
        if reactions:
            print(count)
            return count
        # if no reactions tab, print the resulting shelves
        else:
            print("lower: [%s]" % ', '.join(self.shelf1))
            print("upper: [%s]" % ', '.join(self.shelf2))
            return {'upper': self.shelf2, 'lower': self.shelf1}
