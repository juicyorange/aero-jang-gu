from sklearn import svm
from sklearn.model_selection import train_test_split
import scipy as sp
import os, samples
import joblib
from sklearn.model_selection import GridSearchCV

if __name__ == '__main__':
    x_data = []
    y_data = []

    classes = {}

    root="../data_cut_back_front"
    type_list = ["dda", "duck"]

    print ("Loading the dataset from '{0}'...".format(root)),
    
    # 지정한 폴더에서 데이터 파일을 불러와 학습 진행
    for path, subdirs, files in os.walk(root):
        for name in files:
            filename = os.path.join(path, name)
            # 샘플들을 불러온다
            sample = samples.Sample.load_from_file(filename)
            
            # 데이터를 선형화하여 데이터에 추가
            x_data.append(sample.get_linearized())

            # 카테고리 -> 파일 이름에 포함 ex) dda_sample_1.txt
            category = name.split("_")[0]

            # 라벨링을 위해 type_list에서 해당하는 카테고리의 번호를 찾는다.
            number = type_list.index(category)

            # x_data에 대한 라벨 추가
            y_data.append(number)
            
            classes[number] = category

    print ("DONE")

    # 데이터셋 분리
    X_train, X_test, Y_train, Y_test = train_test_split(x_data, 
                y_data, test_size=0.35, random_state=0)

    # cross validation 에 쓰일 파라미터
    params = {'C':[0.0001 * i for i in range(1, 1000, 5)], 'kernel':['linear']}

    svc = svm.SVC(probability = True)

    # Grid search
    clf = GridSearchCV(svc, params, scoring='accuracy', cv=10, verbose = 10, n_jobs = 8)

    # 학습 시작
    print ("Starting learn process...")
    clf.fit(X_train, Y_train)

    print ("\nBest estimated parameter: ")
    print (clf.best_estimator_)

    score = clf.score(X_test, Y_test)
    print ("\nSCORE: {score}\n".format(score = score))

    print ("Saving the model...",)
    joblib.dump(clf, 'model.pkl') 
    joblib.dump(classes, 'classes.pkl') 

    print ("DONE")