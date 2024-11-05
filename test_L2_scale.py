from L2_Scale_Invariant_2 import L2_Scale_Invariant



ground_truth = [50, 100, 150]
predictions = [45, 110, 140]
n = len(ground_truth)



def test_logarithm():
    log_ground = []
    log_pred = []
    for i in range(n):
        ground_log = L2_Scale_Invariant(ground_truth, predictions).logarithm(ground_truth[i])
        pred_log = L2_Scale_Invariant(ground_truth, predictions).logarithm(predictions[i])
        log_ground.append(ground_log)
        log_pred.append(pred_log)
    assert type(log_ground) == list
    assert type(log_pred) == list
    assert log_ground == [1.6989700043360187, 2.0, 2.1760912590556813]
    assert log_pred == [1.6532125137753437, 2.041392685158225, 2.146128035678238]

def logarithm():
    log_ground = []
    log_pred = []
    for i in range(n):
        ground_log = L2_Scale_Invariant(ground_truth, predictions).logarithm(ground_truth[i])
        pred_log = L2_Scale_Invariant(ground_truth, predictions).logarithm(predictions[i])
        log_ground.append(ground_log)
        log_pred.append(pred_log)
    return log_ground, log_pred

def test_diff():
    log_ground = [1.6989700043360187, 2.0, 2.1760912590556813]
    log_pred = [1.6532125137753437, 2.041392685158225, 2.146128035678238]
    diff_list = []
    for i in range(n):
        diff = L2_Scale_Invariant(ground_truth, predictions).log_diff(log_ground, log_pred)
        diff_list.append(diff)
    assert type(diff_list) == list

def log_diff():
    log_ground = [1.6989700043360187, 2.0, 2.1760912590556813]
    log_pred = [1.6532125137753437, 2.041392685158225, 2.146128035678238]
    diff_list = []
    for i in range(n):
        diff = L2_Scale_Invariant(ground_truth, predictions).log_diff(log_ground[i], log_pred[i])
        diff_list.append(diff) 
    return diff_list

def test_log_squared_diff():
    diff_list = [0.04575749056067502, -0.04139268515822492, 0.02996322337744317]
    diff_log_squared_list = []
    for i in range(n):
        diff_squared = L2_Scale_Invariant(ground_truth, predictions).log_squared_diff(diff_list[i])
        diff_log_squared_list.append(diff_squared)

    assert type(diff_log_squared_list) == list
    assert diff_log_squared_list == [0.0020937479424102635, 0.0017133543846079334, 0.0008977947551665569]
    
def log_squared_diff():
    diff_list = [0.04575749056067502, -0.04139268515822492, 0.02996322337744317]
    diff_log_squared_list = []
    for i in range(n):
        diff_squared = L2_Scale_Invariant(ground_truth, predictions).log_squared_diff(diff_list[i])
        diff_log_squared_list.append(diff_squared)

    return diff_log_squared_list

def test_log_squared_mean():
    squared_diff_list = [0.0020937479424102635, 0.0017133543846079334, 0.0008977947551665569]
    log_squared_mean = L2_Scale_Invariant(ground_truth, predictions).log_squared_mean(squared_diff_list)
    assert type(log_squared_mean) == float
    assert log_squared_mean == 0.0015682990273949181


def log_squared_mean():
    squared_diff_list = [0.0020937479424102635, 0.0017133543846079334, 0.0008977947551665569]
    log_squared_mean = L2_Scale_Invariant(ground_truth, predictions).log_squared_mean(squared_diff_list)
    return log_squared_mean

def test_log_mean():
    diff_list = [0.04575749056067502, -0.04139268515822492, 0.02996322337744317]
    log_mean = L2_Scale_Invariant(ground_truth, predictions).log_mean(diff_list)
    assert type(log_mean) == float
    assert log_mean == 0.011442676259964424

def log_mean():
    diff_list = [0.04575749056067502, -0.04139268515822492, 0.02996322337744317]
    log_mean  = L2_Scale_Invariant(ground_truth, predictions).log_mean(diff_list)
    return log_mean

def test_term_1():
    squared_mean = 0.0015682990273949181
    term_one = L2_Scale_Invariant(ground_truth, predictions).term_1(squared_mean)
    assert type(term_one) == float
    assert term_one == 0.0002613831712324863

def term_1():
    squared_mean = 0.0015682990273949181
    term_one = L2_Scale_Invariant(ground_truth, predictions).term_1(squared_mean)
    return term_one

def test_term_2():
    log_mean = 0.011442676259964424
    term_two = L2_Scale_Invariant(ground_truth, predictions).term_2(log_mean)
    # return term_two

def term_2():
    log_mean = 0.011442676259964424
    term_two = L2_Scale_Invariant(ground_truth, predictions).term_2(log_mean)
    return term_two

if __name__ == "__main__":
    log_ground, log_pred = logarithm()
    print("GROUND LOGS: ", log_ground, "PRED LOGS: ", log_pred)

    diff_list = log_diff()
    print("DIFFERENCE LIST: ", diff_list)

    diff_log_squared_list = log_squared_diff()
    print("DIFFERENCE LOGS SQUARED: ", diff_log_squared_list)

    log_squared_mean = log_squared_mean()
    print("SQUARED LOGS MEAN: ", log_squared_mean)

    log_mean = log_mean()
    print("NORMAL LOG MEAN: ", log_mean)

    term_one = term_1()
    print("TERM 1 TOTAL: ", term_one)

    term_two = term_2()
    print("TERM 2 TOTAL: ", term_two)

    
