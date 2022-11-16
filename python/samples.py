import numpy as np
from sklearn.preprocessing import scale
from scipy.interpolate import interp1d

class Sample:
    '''
    아두이노에서 받아온 raw data를 선형화
    '''
    def __init__(self, acx, acy, acz, gx, gy, gz):
        self.acx = acx
        self.acy = acy
        self.acz = acz
        self.gx = gx
        self.gy = gy
        self.gz = gz

    def get_linearized(self, reshape = False):
        '''
        데이터를 연결하여 제공한다.
        '''
        if reshape:
            return np.concatenate((self.acx, self.acy, self.acz, self.gx, self.gy, self.gz)).reshape(1,-1)
        else:
            return np.concatenate((self.acx, self.acy, self.acz, self.gx, self.gy, self.gz))
		

    @staticmethod
    def load_from_file(filename, size_fit = 100):
        '''
        파일로부터 샘플값들을 받아온다.
        filename: 파일 경로
        size_fit: 선형보간할때 어느정도 샘플수로 할 것인지 결정
        '''

        # filename 에 해당하는 파일에서 값들을 읽어온다.
        data_raw = [list(map(str, i.strip("\n").split(" "))) for i in open(filename)]
        data = np.array(data_raw).astype(float)
        
        # 정규화
        data_norm = scale(data)
        

        # 각 값들을 모아서 불러온다. x축가속도는 x축 가속도만
        acx = data_norm[:,0]
        acy = data_norm[:,1]
        acz = data_norm[:,2]

        gx = data_norm[:,3]
        gy = data_norm[:,4]
        gz = data_norm[:,5]

        
        # x 구간을 생성
        x = np.linspace(0, data.shape[0], data.shape[0])

        # 보간을 위한 함수 생성 y = f(x)
        f_acx = interp1d(x, acx)
        f_acy = interp1d(x, acy)
        f_acz = interp1d(x, acz)

        f_gx = interp1d(x, gx)
        f_gy = interp1d(x, gy)
        f_gz = interp1d(x, gz)

        # size_fit 에 맞게 xnew 구간 생성
        xnew = np.linspace(0, data.shape[0], size_fit)

        # size_fit 에 맞게 sample들을 새로 생성
        acx_stretch = f_acx(xnew)
        acy_stretch = f_acy(xnew)
        acz_stretch = f_acz(xnew)

        gx_stretch = f_gx(xnew)
        gy_stretch = f_gy(xnew)
        gz_stretch = f_gz(xnew)

        return Sample(acx_stretch, acy_stretch, acz_stretch, gx_stretch, gy_stretch, gz_stretch)
    
