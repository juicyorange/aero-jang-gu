import numpy as np
from sklearn.preprocessing import scale
from scipy.interpolate import interp1d

class Sample:
    '''
    mpu6050 raw데이터(ax, ay, az, gx, gy, gz) 로드 및 선형화
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
        선형 데이터 반환
        '''

        weighted_gx = []
        for i in range(0,50):
            weighted_gx.append((self.gx[i])*10)

        if reshape:
            # mpu6050의 모든 데이터 반환
            #return np.concatenate((self.acx, self.acy, self.acz, gx_gradient, self.gy, self.gz)).reshape(1,-1)
            
            # gx 데이터만 반환
            return np.array(weighted_gx).reshape(1,-1)
        else:
            # mpu6050의 모든 데이터
            #return np.concatenate((self.acx, self.acy, self.acz, gx_gradient, self.gy, self.gz))
            
            # gx 데이터만 반환
            return np.array(weighted_gx)
        

    @staticmethod
    def load_from_file(filename, size_fit = 50):
        '''
        파일에서 데이터를 읽어오고 데이터 보간을 통해 데이터의 수를 일치시킨다

        filename: 파일 경로
        size_fit: 보간을 통해 맞춰 줄 데이터 수
        '''

        data_raw = [list(map(str, i.strip("\n").split(" "))) for i in open(filename)]
        data = np.array(data_raw).astype(float)
        
        # 정규화
        data_norm = scale(data)
        
        acx = data_norm[:,0]
        acy = data_norm[:,1]
        acz = data_norm[:,2]

        gx = data_norm[:,3]
        gy = data_norm[:,4]
        gz = data_norm[:,5]

        # 기존 x 데이터
        x = np.linspace(0, data.shape[0], data.shape[0])

        # 보간 함수 function y = f(x)
        f_acx = interp1d(x, acx)
        f_acy = interp1d(x, acy)
        f_acz = interp1d(x, acz)

        f_gx = interp1d(x, gx)
        f_gy = interp1d(x, gy)
        f_gz = interp1d(x, gz)

        # 새로운 x 데이터 (size_fit)
        xnew = np.linspace(0, data.shape[0], size_fit)

        # size_fit 에 따라 데이터 조정
        acx_stretch = f_acx(xnew)
        acy_stretch = f_acy(xnew)
        acz_stretch = f_acz(xnew)

        gx_stretch = f_gx(xnew)
        gy_stretch = f_gy(xnew)
        gz_stretch = f_gz(xnew)

        return Sample(acx_stretch, acy_stretch, acz_stretch, gx_stretch, gy_stretch, gz_stretch)
    
    @staticmethod
    def load_from_list(data_raw, size_fit = 50):
        '''
        리스트를 받아 데이터 보간을 통해 데이터의 수를 일치시킨다
        '''
        data = np.array(data_raw).astype(float)
        data_norm = scale(data)

        acx = data_norm[:,0]
        acy = data_norm[:,1]
        acz = data_norm[:,2]

        gx = data_norm[:,3]
        gy = data_norm[:,4]
        gz = data_norm[:,5]

        x = np.linspace(0, data.shape[0], data.shape[0])
        f_acx = interp1d(x, acx)
        f_acy = interp1d(x, acy)
        f_acz = interp1d(x, acz)

        f_gx = interp1d(x, gx)
        f_gy = interp1d(x, gy)
        f_gz = interp1d(x, gz)

        xnew = np.linspace(0, data.shape[0], size_fit)
        acx_stretch = f_acx(xnew)
        acy_stretch = f_acy(xnew)
        acz_stretch = f_acz(xnew)

        gx_stretch = f_gx(xnew)
        gy_stretch = f_gy(xnew)
        gz_stretch = f_gz(xnew)

        return Sample(acx_stretch, acy_stretch, acz_stretch, gx_stretch, gy_stretch, gz_stretch)

