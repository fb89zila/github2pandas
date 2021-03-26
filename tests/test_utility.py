#!/usr/bin/python
 
import unittest
import sys
import os
from pathlib import Path
import warnings

from github2pandas.utility import Utility

class TestUtility(unittest.TestCase):
    
    github_token = os.environ['TOKEN']

    git_repo_name = "Extract_Git_Activities"
    git_repo_owner = "TUBAF-IFI-DiPiT"
    default_data_folder = Path("data", git_repo_name)

    def test_get_repo(self):
        """
        Evaluate accessibility of repository 
        """
        warnings.simplefilter ("ignore", ResourceWarning)
        repo = Utility.get_repo(self.git_repo_owner, self.git_repo_name, self.github_token, self.default_data_folder)
        self.assertIsNotNone(repo)

    def test_github_token_availability(self):
        self.assertTrue( "TOKEN" in os.environ , "No Token available")


if __name__ == "__main__":
    unittest.main()
