
import os
import re
import unittest
from compile import compile


class TestIntegrationCompile(unittest.TestCase):
    output_file_path = "./out.cs"
    source_file_path = "./src/tests/delete_me.txt"

    def test_compile_complex(self):

        source_code="""
        num a := 1
        num b := 1
        num c := 1
        while 1>2{
            num a := 2 
            b := 2
        } 
        /* i am a comment ///// \\\\\ ****
        asdf 
        asdf
        */
        bool idxyz
        bool idxzy := true
        /* list subscripting */
        num[] atest := {0}
        atest [0] := 1
        num[][][] btest := {{{0}}}
        btest [0][0][0] := 1
        btest [0][0] := {1}
        btest [0][0] := {1}
        /* func call */
        num functest123(){
            return 1
        }
        funcxyz(num a,num b){}
        funcxyz(a+3,functest123())
        /* check if floats, ints, and signed numbers work */
        a := 0.9
        a := -0.9
        a := 9
        a := -9
        while a > b {
            /*print(a)*/
            } 
        num aa := 1
        num a1 := 1
        num _a1 := 1
        string ssss:="________lisdahf98764876aosdifhalidsfh8762467______a1"
        num ________lisdahf98764876aosdifhalidsfh8762467______a1 := 1

        if 1 > 2 {}
        else if 1>2 {}
        else {}
        num iasdhf(){
            return 1
        }
        bool booly := true
        """
        expected_cs_code = """
        using System.Collections.Generic;
        using System;
        class Program {
            static double a = 1.0;
            static double b = 1.0;
            static double c = 1.0;
            static bool idxyz;
            static bool idxzy = true;
            static List<double> atest = new List<double>(){0.0};
            static List<List<List<double>>> btest = new List<List<List<double>>>(){new List<List<double>>(){new List<double>(){0.0}}};
            static double aa = 1.0;
            static double a1 = 1.0;
            static double _a1 = 1.0;
            static String ssss = "________lisdahf98764876aosdifhalidsfh8762467______a1";
            static double ________lisdahf98764876aosdifhalidsfh8762467______a1 = 1.0;
            static bool booly = true;
            static public double functest123(){
                return 1.0;
            }
            static public void funcxyz(double a,double b){
            }
            static public double iasdhf(){
                return 1.0;
            }
            static public void Main(){
                while (1.0>2.0){
                    double a = 2.0;
                    b = 2.0;
                }
                atest[0] = 1.0;
                btest[0][0][0] = 1.0;
                btest[0][0] = new List<double>(){1.0};
                btest[0][0] = new List<double>(){1.0};
                funcxyz(a+3.0,functest123());
                a = 0.9;
                a = -0.9;
                a = 9.0;
                a = -9.0;
                while (a>b){
                }
                if (1.0>2.0){
                }
                else if (1.0>2.0){
                }
            }
        }
        """
        self.integration_test(source_code, expected_cs_code)

    def test_compile_simple(self):
        source_code = """
        num a := 5
        num b := 6
        num c := a + b
        """
        expected_cs_code = """
        using System.Collections.Generic;
        using System;
        class Program {
            static double a = 5.0;
            static double b = 6.0;
            static double c = a+b;
            static public void Main(){
            }
        }"""
        self.integration_test(source_code, expected_cs_code)

    def integration_test(self, source_code, expected_cs_code):
        # create temporary file
        self.write_file(self.source_file_path, source_code)
        # compile the temporary file
        compile(self.source_file_path)
        # delete the temporary file
        self.delete_file(self.source_file_path)
        # read the output file
        actual_cs_code = self.read_file(self.output_file_path)
        # format the expected and actual code to a unified format (remove whitespace)
        expected = self.unify_whitespace_in_string(expected_cs_code)
        actual = self.unify_whitespace_in_string(actual_cs_code)
        # assert 
        self.assertEqual(expected, actual)

    def unify_whitespace_in_string(self, s: str) -> str:
        return re.sub(r"\s+", " ", s).strip()

    def read_file(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()

    def write_file(self, path: str, content: str):
        with open(path, "w") as f:
            f.write(content)

    def delete_file(self, path: str):
        os.remove(path)
