import unittest
from rule_engine import create_rule, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_rule_creation(self):
        rule_string = "age > 30 AND (department = 'Sales' OR salary > 50000)"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

    def test_rule_evaluation(self):
        data = {"age": 35, "department": "Sales", "salary": 60000}
        rule_string = "age > 30 AND (department = 'Sales' OR salary > 50000)"
        ast = create_rule(rule_string)
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
