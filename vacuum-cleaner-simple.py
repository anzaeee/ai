# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Environment():
    def __init__(self):
        # 0 means clean and 1 means dirty
        self.location = {'A': '0', 'B': '0', 'C': '0'}


class VacuumAgent(Environment):
    PM = 0  # set performance measure to 0
    position = '0'

    def Clean(self,Environment):
        # if initial is A
        if self.position == 'A':
            # print('Vacuum currently placed at A. State is: ' + print_CleanDirty(position) )
            if Environment.location['A'] == '0':
                print('')
            elif Environment.location['A'] == '1':
                Environment.location['A'] = 0
                self.PM += 1

            # move to B
            self.PM += 1

            # check B
            if Environment.location['B'] == '0':
                print('Area is already clean. Moving to C')
            if Environment.location['B'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['B'] = 0
                self.PM += 1


            # move to C
            self.PM += 1

            if Environment.location['C'] == '0':
                print('Area is already clean.')
            if Environment.location['C'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['C'] = 0
                self.PM += 1

        # if initial is B
        elif self.position == 'B':
            # print('Vacuum currently placed at B. State is: ' + print_CleanDirty(position) )
            if Environment.location['B'] == '0':
                print('Area is already clean. Moving to A')
            elif Environment.location['B'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['B'] = 0
                self.PM += 1

            # move to C
            print('Moving to C')
            self.PM += 1

            # check if C is clean
            if Environment.location['C'] == '0':
                print('Area is already clean. Moving to A')
            if Environment.location['C'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['C'] = 0
                self.PM += 1

            # move to A
            print('Moving to A')
            self.PM += 1

            # check if C is clean
            if Environment.location['A'] == '0':
                print('Area is already clean.')
            if Environment.location['A'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['A'] = 0
                self.PM += 1

        # if initial is C
        elif self.position == 'C':
        #print('Vacuum currently placed at B. State is: ' + print_CleanDirty(position) )

            if Environment.location['C'] == '0':
                print('Area is already clean. Moving to A')
            elif Environment.location['C'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['C'] = 0
                self.PM += 1

            # move to A
            print('Moving to A')
            self.PM += 1

            # check if A is clean
            if Environment.location['A'] == '0':
                print('Area is already clean. Moving to B')
            if Environment.location['A'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['A'] = 0
                self.PM += 1

            # move to B
            print('Moving to B')
            self.PM += 1

            # check if B is clean
            if Environment.location['B'] == '0':
                print('Area is already clean.')
            if Environment.location['B'] == '1':
                print('Area is dirty. Clean clean clean')
                Environment.location['B'] = 0
                self.PM += 1

        print(Environment.location)
        print('cleaning is done')
        print('Performance measure: ' + str(self.PM))


if __name__ == '__main__':
    initial_loc = input('Enter location of vacuum (A/B/C) ')
    X = Environment()
    VC = VacuumAgent()
    VC.position = initial_loc

    if initial_loc == 'A':
        X.location.update({'A': input('Enter state of ' + initial_loc + ' (0/1): ')})
        X.location.update({'B': input('Enter state of B (0/1) :')})
        X.location.update({'C': input('Enter state of C (0/1) :')})
    if initial_loc == 'B':
        X.location.update({'B': input('Enter state of ' + initial_loc + ' (0/1): ')})
        X.location.update({'A': input('Enter state of A (0/1): ')})
        X.location.update({'C': input('Enter state of C (0/1): ')})
    if initial_loc == 'C':
        X.location.update({'C': input('Enter state of ' + initial_loc + ' (0/1): ')})
        X.location.update({'A': input('Enter state of A (0/1): ')})
        X.location.update({'B': input('Enter state of B (0/1): ')})

    VC.Clean(X)

    # Press the green

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
