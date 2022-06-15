
class Evaluator:

    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            print("-1")
            return -1
        print(sum((t[0]*len(t[1])) for t in zip(coefs, words)))

    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            print("-1")
            return -1
        print(sum((t[0]*len(t[1])) for t in enumerate(coefs, words)))


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.enumerate_evaluate(coefs, words)
