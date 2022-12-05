# run tests

import prob_calculator


#prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=3, red=4, green=2)

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=10)

#print("Probability:", probability)




