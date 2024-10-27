from SSUphysicsTools.getting_data import get_all_csv_paths_in_data, read_csv_Tektronix
import numpy as np
from pandas import DataFrame
from typing import Optional
import matplotlib.pyplot as plt
import os

class Plots(get_all_csv_paths_in_data):
    def __init__(self,plot_name:tuple[str], flatten:Optional[bool]=False,directory:Optional[str]='data'):
        '''
        :param plot_name: tuple[str], the name of the plots.
        '''
        super().__init__(flatten=flatten,directory=directory)
        self.plot_name = plot_name
    
    # plots
    def orginal_data_plots(self, is_save:Optional[bool]=False,dpi:Optional[int]=300):
        '''
        Automaticaly plots the original data generated by Tektronix.
        :param is_save: bool, save the plots or not. no support for flatten=True.
        > warning: no support for flatten=True yet.
        '''
        plot_name=self.plot_name
        flatten=self.flatten
        all_csv_list=self.all_csv_list

        if flatten:
            for csv in all_csv_list:
                results = read_csv_Tektronix(csv)
                data=results['data']
                plt.plot(data['Time'], data['Voltage'])
                plt.xlabel('Time (s)')
                plt.ylabel('Voltage (V)')
                plt.show()
                plt.close()

        # flatten=False
        all_csv_list=all_csv_list
        assert len(plot_name)==len(all_csv_list), 'The number of plot names should be the same as the number of csv files.'

        for i,csv_list in enumerate(all_csv_list):
            results = np.array([read_csv_Tektronix(csv_list[0]),read_csv_Tektronix(csv_list[1])])
            data1=results[0]['data']
            data2=results[1]['data']
            plt.plot(data1['Time'], data1['Voltage'])
            plt.plot(data2['Time'], data2['Voltage'])
            plt.xlabel('Time (s)')
            plt.ylabel('Voltage (V)')
            plt.legend(['CH1', 'CH2'])
            plt.title(f'{plot_name[i]}')
            for ii in (0,):
                plt.axhline(y=ii, color='gray', zorder=-1)
            plt.axvline(x=0, color='gray', zorder=-1)
            if is_save:
                print(f'Saving {plot_name[i]}')
                plt.savefig(f'fig/{plot_name[i]}.png',dpi=dpi)
            plt.show()
            plt.close()
            
    
    def bode_plots(self):
        assert self.flatten==False, 'The flatten should be False to use bode_plots method.'
        plot_name=self.plot_name
        all_csv_list=self.all_csv_list

        for i,csv_list in enumerate(all_csv_list):
            results = np.array([read_csv_Tektronix(csv_list[0]),read_csv_Tektronix(csv_list[1])])
            data1=results[0]['data']
            data2=results[1]['data']
            plt.plot(data1['Time'], data1['Voltage'])
            plt.plot(data2['Time'], data2['Voltage'])
            plt.xlabel('Time (s)')
            plt.ylabel('Voltage (V)')
            plt.legend(['CH1', 'CH2'])
            plt.title(f'{plot_name[i]}')
            for i in (-1,0,1):
                plt.axhline(y=i, color='gray', zorder=-1)
            plt.axvline(x=0, color='gray', zorder=-1)
            plt.show()
            plt.close()

def plot_table(data:DataFrame, title:str, table_font_size:Optional[int]=8,save_dir:Optional[str]=None ,is_save:Optional[bool]=False)->None:
    """
    데이터프레임을 테이블 형태로 시각화합니다.
    :param data: 데이터프레임
    :param title: 테이블 제목
    :param save_dir: 저장 경로, is_save가 True일 때만 사용, None일 때는 project root directory에 저장
    :param is_save: 저장 여부
    :return: None
    """
    # data의 모든 값을 문자열로 변환
    data=data.astype(str)

    # 그림과 축 생성
    fig, ax = plt.subplots()

    # 축을 숨김
    ax.axis('tight')
    ax.axis('off')

    # 테이블 생성
    table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

    # 헤더 셀 음영 처리
    for key, cell in table.get_celld().items():
        if key[0] == 0:  # 헤더 행
            cell.set_facecolor('#D3D3D3')  # 연한 회색
            cell.set_text_props(weight='bold')  # 텍스트 굵게 설정
        

    table.set_fontsize(table_font_size)  # 테이블 전체 폰트 크기 설정
    table.auto_set_font_size(False)  # 폰트 크기 자동 조정 비활성화
    table.auto_set_column_width(col=list(range(len(data.columns))))  # 셀 너비 자동 조정 비활성화
    title_font = {'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Times New Roman','color': 'black'}
    ax.set_title(title,fontdict=title_font)
    plt.tight_layout()
    plt.show()
    if is_save:
        if save_dir is None:
            save_dir = './'
            plt.savefig(f'{title}.png', bbox_inches='tight', dpi=300)

        else: # 저장하지 않을 경우 그림 닫기
            plt.savefig(f'{save_dir}/{title}.png', bbox_inches='tight', dpi=300)

    plt.close()