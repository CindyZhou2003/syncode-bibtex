import unittest
from lark import Lark
import os

class TestBibTeXGrammar(unittest.TestCase):
    def setUp(self):
        # Load the grammar file
        with open('bibtex.lark', 'r') as f:
            grammar = f.read()
        
        # Create a parser
        self.parser = Lark(grammar, start='bibTex', parser='lalr')
    
    def test_article(self):
        """Test parsing a standard article entry."""
        bibtex = '''
        @article{Smith2020,
            author = {John Smith},
            title = {A Study of Something Interesting and Novel},
            journal = {Journal of Important Studies},
            year = {2020},
            volume = {10},
            number = {2},
            pages = {100-120},
            doi = {10.1234/example.doi}
        }
        '''
        # Assert no exception is raised
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)
    
    def test_book_with_complex_fields(self):
        """Test parsing a book with complex fields including edition and ISBN."""
        bibtex = '''
        @book{Johnson2019,
            author = {Emily Johnson and David Thompson},
            title = {The Complete Guide to Everything},
            publisher = {Academic Publishing House},
            year = {2019},
            edition = {2nd},
            isbn = {978-0-12-345678-9},
            address = {New York, NY},
            note = {With additional commentary}
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)
    
    def test_complex_author_list(self):
        """Test parsing an entry with a complex author list."""
        bibtex = '''
        @article{MultiAuthor2021,
            author = {James Smith and Emily Johnson and Robert Brown and Jennifer Davis and Michael Wilson and Maria García-López},
            title = {Collaborative Research on Complex Topics},
            journal = {Science Journal},
            year = {2021},
            volume = {15},
            number = {3},
            pages = {200-215},
            keywords = {collaboration, interdisciplinary, research methods}
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)
    
    def test_with_quotes_and_mixed_formats(self):
        """Test parsing an entry using quotes for some values and braces for others."""
        bibtex = '''
        @inproceedings{Conference2020,
            author = {David Miller},
            title = "Advances in Technology and Computing",
            booktitle = {Proceedings of the Annual Conference on Innovation},
            year = "2020",
            month = "June",
            pages = {45-52},
            publisher = {IEEE},
            address = "San Francisco, CA"
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)
    
    def test_with_special_characters(self):
        """Test parsing an entry with special LaTeX characters and commands."""
        bibtex = '''
        @article{Special2018,
            author = {M{\\\"u}ller, Andreas and Garc{\\'i}a, Jos{\\'e}},
            title = {Research with Sp\\^ecial Ch\\`aracters and Symbols: $\\alpha$, $\\beta$, $\\gamma$},
            journal = {International Journal of Science},
            year = {2018},
            volume = {42},
            number = {1},
            pages = {1-15},
            note = {Contains \\textbf{bold}, \\textit{italic}, and $\\sum_{i=1}^{n} x_i$ mathematical notation}
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)
    
    def test_multiple_entries_and_types(self):
        """Test parsing multiple entries of different types in a single file."""
        bibtex = '''
        @article{Smith2020,
            author = {John Smith},
            title = {A Study of Something},
            journal = {Journal of Studies},
            year = {2020}
        }
        
        @book{Johnson2019,
            author = {Emily Johnson},
            title = {The Complete Guide},
            publisher = {Academic Press},
            year = {2019}
        }
        
        @inproceedings{Conference2020,
            author = {David Miller},
            title = {Advances in Technology},
            booktitle = {Proceedings of the Annual Conference},
            year = {2020},
            publisher = {IEEE}
        }
        
        @phdthesis{Roberts2018,
            author = {Sarah Roberts},
            title = {Novel Approaches to Theoretical Problems},
            school = {University of Research},
            year = {2018},
            type = {PhD Thesis}
        }
        
        @techreport{Tech2021,
            author = {Technical Team},
            title = {Implementation Report},
            institution = {Research Institute},
            year = {2021},
            number = {TR-2021-01}
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)

    def test_provided_examples(self):
        """Test parsing the provided examples from the assignment."""
        bibtex = '''
        @article{ding_bloccess_2023,
            title = {Bloccess: {Enabling} {Fine}-{Grained} {Access} {Control} {Based} on {Blockchain}},
            volume = {31},
            url = {https://link.springer.com/article/10.1007/s10922-022-09700-5},
            doi = {10.1007/s10922-022-09700-5},
            number = {1},
            journal = {Journal of Network and Systems Management},
            author = {Ding, Yepeng and Sato, Hiroyuki},
            year = {2023},
            pages = {1--34},
        }
        @inproceedings{ding_self-sovereign_2022,
            title = {Self-{Sovereign} {Identity} as a {Service}: {Architecture} in {Practice}},
            copyright = {All rights reserved},
            isbn = {978-1-66548-810-5},
            doi = {10.1109/COMPSAC54236.2022.00244},
            booktitle = {2022 {IEEE} 46th {Annual} {Computers}, {Software}, and {Applications} {Conference} ({COMPSAC})},
            publisher = {IEEE},
            author = {Ding, Yepeng and Sato, Hiroyuki},
            year = {2022},
            pages = {1537--1543},
        }
        @article{ding_formalism-driven_2022,
            title = {Formalism-{Driven} {Development}: {Concepts}, {Taxonomy}, and {Practice}},
            volume = {12},
            issn = {2076-3417},
            url = {https://www.mdpi.com/2076-3417/12/7/3415},
            doi = {10.3390/app12073415},
            number = {7},
            journal = {Applied Sciences},
            author = {Ding, Yepeng and Sato, Hiroyuki},
            year = {2022},
        }
        '''
        result = self.parser.parse(bibtex)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
