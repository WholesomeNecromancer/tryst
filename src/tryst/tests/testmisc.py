# testmisc.py
# Copyright 2021 Travis Gates

# In addition to the below license information, Toolshed files must contain
# The 7 fundamental tenets of the Satanic Temple prior to any code:
# 1. One should strive to act with compassion and empathy toward all creatures in accordance with reason.
# 2. The struggle for justice is an ongoing and necessary pursuit that should prevail over laws and institutions.
# 3. One's body is inviolable, subject to one's own will alone.
# 4. The freedom of others should be respected, including the freedom to offend. To willfully and unjustly encroach upon the freedoms of another is to forgo one's own.
# 5. Beliefs should conform to one's best scientific understanding of the world. One should take care never to distort scientific facts to fit one's beliefs.
# 6. People are fallible. If one makes a mistake, one should do one's best to rectify it and resolve any harm that might have been caused.
# 7. Every tenet is a guiding principle designed to inspire nobility in action and thought. The spirit of compassion, wisdom, and justice should always prevail over the written or spoken word.

# This file is part of Toolshed.

# Toolshed is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Toolshed is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Toolshed.  If not, see <https://www.gnu.org/licenses/>.

import json
import unittest
from tryst import Tryst
from tryst import Option
import os

class TestTryst(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Whatever setup should happen before any tests in this class
        pass

    @classmethod
    def tearDownClass(self):
        # Whatever cleanup should occur after all tests in this class
        pass

    def setUp(self):
        # Setup that will be performed before EACH test* function
        self.tryst = Tryst()

    def tearDown(self):
        # Cleanup performed after EACH test* function
        pass

    def testlistremoval(self):
        thing3 = {}
        thing3["key"] = "value"
        thing3["key2"] = True
        things = ["thing1", "thing2", thing3]

        print("before removal: " + str(things))
        for thing in things:
            if isinstance(thing, dict):
                things.remove(thing)
        print("after removal: " + str(things))

        pass

#----------------------------------------
if __name__ == "__main__":
    # This basically instructs the Python package unittest to do all its work --
    # assemble test cases into a suite and run them.
    unittest.main()
#----------------------------------------