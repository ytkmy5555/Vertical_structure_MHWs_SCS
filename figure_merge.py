import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.cm as cm

data1 = np.load('./Sf.npz')
data1.files

data2 = np.load('./Adv.npz')
data2.files

data3 = np.load('./Tt.npz')
data3.files

Shallow_sf_mean = data1['Shallow_sf_mean'][:]
Subsurface_reversed_sf_mean = data1['Subsurface_reversed_sf_mean'][:]
Subsurface_intensified_sf_mean = data1['Subsurface_intensified_sf_mean'][:]
Deep_sf_mean = data1['Deep_sf_mean'][:]
Subsurface_intensified_Reversed_sf_mean = data1['Subsurface_intensified_Reversed_sf_mean'][:]

Shallow_adv_mean = data2['Shallow_sf_mean'][:]
Subsurface_reversed_adv_mean = data2['Subsurface_reversed_sf_mean'][:]
Subsurface_intensified_adv_mean = data2['Subsurface_intensified_sf_mean'][:]
Deep_adv_mean = data2['Deep_sf_mean'][:]
Subsurface_intensified_Reversed_adv_mean = data2['Subsurface_intensified_Reversed_sf_mean'][:]

Shallow_Tt_mean = data3['Shallow_sf_mean'][:]
Subsurface_reversed_Tt_mean = data3['Subsurface_reversed_sf_mean'][:]
Subsurface_intensified_Tt_mean = data3['Subsurface_intensified_sf_mean'][:]
Deep_Tt_mean = data3['Deep_sf_mean'][:]
Subsurface_intensified_Reversed_Tt_mean = data3['Subsurface_intensified_Reversed_sf_mean'][:]

Shallow_Res = Shallow_Tt_mean[:,:240] - Shallow_adv_mean[:,:240] - Shallow_sf_mean
Reversed_Res = Subsurface_reversed_Tt_mean[:,:240] - Subsurface_reversed_adv_mean[:,:240] - Subsurface_reversed_sf_mean
Intensified_Res = Subsurface_intensified_Tt_mean[:,:240] - Subsurface_intensified_adv_mean[:,:240] - Subsurface_intensified_sf_mean
Deep_Res = Deep_Tt_mean[:,:240] - Deep_adv_mean[:,:240] - Deep_sf_mean
Intensified_Reversed_Res = Subsurface_intensified_Reversed_Tt_mean[:,:240] - Subsurface_intensified_Reversed_adv_mean[:,:240] - Subsurface_intensified_Reversed_sf_mean

Tt = np.concatenate((Shallow_Tt_mean.reshape(1,241,241),
                    Subsurface_reversed_Tt_mean.reshape(1,241,241),
                    Subsurface_intensified_Tt_mean.reshape(1,241,241),
                    Deep_Tt_mean.reshape(1,241,241),
                    Subsurface_intensified_Reversed_Tt_mean.reshape(1,241,241),))

adv = np.concatenate((Shallow_adv_mean.reshape(1,241,241),
                      Subsurface_reversed_adv_mean.reshape(1,241,241),
                      Subsurface_intensified_adv_mean.reshape(1,241,241),
                      Deep_adv_mean.reshape(1,241,241),
                      Subsurface_intensified_Reversed_adv_mean.reshape(1,241,241),
))

Sf = np.concatenate((Shallow_sf_mean.reshape(1,241,240),
                     Subsurface_reversed_sf_mean.reshape(1,241,240),
                     Subsurface_intensified_sf_mean.reshape(1,241,240),
                     Deep_sf_mean.reshape(1,241,240),
                     Subsurface_intensified_Reversed_sf_mean.reshape(1,241,240),
))

Res = np.concatenate((Shallow_Res.reshape(1,241,240),
                     Reversed_Res.reshape(1,241,240),
                     Intensified_Res.reshape(1,241,240),
                     Deep_Res.reshape(1,241,240),
                     Intensified_Reversed_Res.reshape(1,241,240),
))

Shallow_adv_mean[Subsurface_reversed_adv_mean == np.inf] = np.nan
np.nanmean(Subsurface_reversed_adv_mean)

Tt_mean = np.nanmean(Tt, axis = 0)
adv_mean = np.nanmean(adv, axis = 0)
Sf_mean = np.nanmean(Sf, axis = 0)
Res_mean = np.nanmean(Res, axis = 0)

fig, axarr = plt.subplots(4, 6, figsize=(20, 15), dpi=300)

data1 = Tt_mean[:240,:240]
data2 = Shallow_Tt_mean[:240,:240]
data3 = Subsurface_reversed_Tt_mean[:240,:240]
data4 = Subsurface_intensified_Tt_mean[:240,:240]
data5 = Deep_Tt_mean[:240,:240]
data6 = Subsurface_intensified_Reversed_Tt_mean[:240,:240]

data1 = np.where(data1==0, np.nan, data1)
data2 = np.where(data2==0, np.nan, data2)
data3 = np.where(data3==0, np.nan, data3)
data4 = np.where(data4==0, np.nan, data4)
data5 = np.where(data5==0, np.nan, data5)
data6 = np.where(data6==0, np.nan, data6)

data21 = Sf_mean[:240,:240]
data22 = Shallow_sf_mean[:240,:240]
data23 = Subsurface_reversed_sf_mean[:240,:240]
data24 = Subsurface_intensified_sf_mean[:240,:240]
data25 = Deep_sf_mean[:240,:240]
data26 = Subsurface_intensified_Reversed_sf_mean[:240,:240]

data21 = np.where(data1==0, np.nan, data21)
data22 = np.where(data2==0, np.nan, data22)
data23 = np.where(data3==0, np.nan, data23)
data24 = np.where(data4==0, np.nan, data24)
data25 = np.where(data5==0, np.nan, data25)
data26 = np.where(data6==0, np.nan, data26)

data31 = adv_mean[:240,:240]
data32 = Shallow_adv_mean[:240,:240]
data33 = Subsurface_reversed_adv_mean[:240,:240]
data34 = Subsurface_intensified_adv_mean[:240,:240]
data35 = Deep_adv_mean[:240,:240]
data36 = Subsurface_intensified_Reversed_adv_mean[:240,:240]

data31 = np.where(data1==0, np.nan, data31)
data32 = np.where(data2==0, np.nan, data32)
data33 = np.where(data3==0, np.nan, data33)
data34 = np.where(data4==0, np.nan, data34)
data35 = np.where(data5==0, np.nan, data35)
data36 = np.where(data6==0, np.nan, data36)

data41 = Res_mean[:240,:240]
data42 = Shallow_Res[:240,:240]
data43 = Reversed_Res[:240,:240]
data44 = Intensified_Res[:240,:240]
data45 = Deep_Res[:240,:240]
data46 = Intensified_Reversed_Res[:240,:240]

data41 = np.where(data1==0, np.nan, data41)
data42 = np.where(data2==0, np.nan, data42)
data43 = np.where(data3==0, np.nan, data43)
data44 = np.where(data4==0, np.nan, data44)
data45 = np.where(data5==0, np.nan, data45)
data46 = np.where(data6==0, np.nan, data46)

colors = ['#1d4c8b', '#2352A0', '#2f69b1', '#3677a4', '#4283bd', '#579ac9', '#6cabe2', '#7db3d7', '#8fc4dc',
'#a2cbe3', '#b5d4e6', '#c0dbec', '#cbe3f3', '#dbe9f1','#eef2f5',
          '#fefefe',
'#fffaf3', '#fff4ea', '#ffeacc', '#ffd9c1', '#ffcfae', '#ffbf9e', '#ffbfa0',
'#f7aba0', '#f3a89a', '#f0a093', '#eb998c', '#e69185', '#e68b7e', '#db6f6d', '#da6e6d',
'#d26967', '#c9615d'
          ]
cmap_custom = ListedColormap(colors)
cmap_custom.set_bad(color='lightgrey')

norm_data2 = BoundaryNorm([-0.15, -0.14, -0.13, -0.12, -0.11, -0.10, -0.09, -0.08, -0.07, -0.06,
                     -0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01,
                     0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12,
                     0.13, 0.14, 0.15], cmap_custom.N)

sm_data2 = cm.ScalarMappable(cmap=cmap_custom, norm=norm_data2)
sm_data2.set_array([])

axarr[0,0].imshow(data1, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[0,1].imshow(data2, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[0,2].imshow(data3, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[0,3].imshow(data4, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[0,4].imshow(data5, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[0,5].imshow(data6, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


axarr[1,0].imshow(data21, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[1,1].imshow(data22, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[1,2].imshow(data23, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[1,3].imshow(data24, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[1,4].imshow(data25, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[1,5].imshow(data26, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

axarr[2,0].imshow(data31, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[2,1].imshow(data32, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[2,2].imshow(data33, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[2,3].imshow(data34, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[2,4].imshow(data35, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[2,5].imshow(data36, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

axarr[3,0].imshow(data41, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[3,1].imshow(data42, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[3,2].imshow(data43, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[3,3].imshow(data44, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[3,4].imshow(data45, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
axarr[3,5].imshow(data46, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

axarr[0,0].set_xticks([])
axarr[0,0].set_yticks([])
axarr[0,1].set_xticks([])
axarr[0,1].set_yticks([])
axarr[0,2].set_xticks([])
axarr[0,2].set_yticks([])
axarr[0,3].set_xticks([])
axarr[0,3].set_yticks([])
axarr[0,4].set_xticks([])
axarr[0,4].set_yticks([])
axarr[0,5].set_xticks([])
axarr[0,5].set_yticks([])

axarr[1,0].set_xticks([])
axarr[1,0].set_yticks([])
axarr[1,1].set_xticks([])
axarr[1,1].set_yticks([])
axarr[1,2].set_xticks([])
axarr[1,2].set_yticks([])
axarr[1,3].set_xticks([])
axarr[1,3].set_yticks([])
axarr[1,4].set_xticks([])
axarr[1,4].set_yticks([])
axarr[1,5].set_xticks([])
axarr[1,5].set_yticks([])

axarr[2,0].set_xticks([])
axarr[2,0].set_yticks([])
axarr[2,1].set_xticks([])
axarr[2,1].set_yticks([])
axarr[2,2].set_xticks([])
axarr[2,2].set_yticks([])
axarr[2,3].set_xticks([])
axarr[2,3].set_yticks([])
axarr[2,4].set_xticks([])
axarr[2,4].set_yticks([])
axarr[2,5].set_xticks([])
axarr[2,5].set_yticks([])

axarr[3,0].set_xticks([])
axarr[3,0].set_yticks([])
axarr[3,1].set_xticks([])
axarr[3,1].set_yticks([])
axarr[3,2].set_xticks([])
axarr[3,2].set_yticks([])
axarr[3,3].set_xticks([])
axarr[3,3].set_yticks([])
axarr[3,4].set_xticks([])
axarr[3,4].set_yticks([])
axarr[3,5].set_xticks([])
axarr[3,5].set_yticks([])


plt.subplots_adjust(right=0.88)  
# cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])  
cbar_ax = fig.add_axes([0.84, 0.16, 0.013, 0.7]) 
cbar = fig.colorbar(sm_data2, cax=cbar_ax, shrink=0.85)
cbar.set_ticks([-0.15, -0.05, 0.05, 0.15])
cbar.set_ticklabels([-0.15, -0.05, 0.05, 0.15])
cbar.set_label('℃/day', rotation=0, labelpad=-40, fontsize=8)
cbar.ax.yaxis.set_label_coords(0.7, -0.03)

plt.subplots_adjust(wspace=-0.5, hspace=0.2) 

axarr[0,0].imshow(data1, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,0].set_title('Tt', fontdict={'fontsize': 3})
axarr[0,0].text(0.30, 1.03, 'Average', transform=axarr[0,0].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')

axarr[0,1].imshow(data2, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,1].set_title('Shallow MHWs Tt',fontdict={'fontsize': 3})
axarr[0,1].text(0.3, 1.03, 'Shallow', transform=axarr[0,1].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')

axarr[0,2].imshow(data3, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,2].set_title('Reversed MHWs Tt',fontdict={'fontsize': 3})
axarr[0,2].text(0.28, 1.03, 'Reversed', transform=axarr[0,2].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')

axarr[0,3].imshow(data4, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,3].set_title('Intensified MHWs Tt',fontdict={'fontsize': 3})
axarr[0,3].text(0.26, 1.03, 'Intensified', transform=axarr[0,3].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')

axarr[0,4].imshow(data5, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,4].set_title('Deep MHWs Tt',fontdict={'fontsize': 3})
axarr[0,4].text(0.38, 1.03, 'Deep', transform=axarr[0,4].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')

axarr[0,5].imshow(data6, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[0,5].set_title('Intensified_Reversed MHWs Tt',fontdict={'fontsize': 3})
axarr[0,5].text(0.02, 1.03, 'Intensified_Reversed', transform=axarr[0,5].transAxes, fontsize=6, fontweight='bold',fontname='Times New Roman')


axarr[1,0].imshow(data21, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,0].set_title('Sf', fontdict={'fontsize': 10})
# axarr[1,0].text(0.5, 1.03, 'Sf', transform=axarr[1,0].transAxes, fontsize=4, fontname='Times New Roman')

axarr[1,1].imshow(data22, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,1].set_title('Shallow MHWs Sf',fontdict={'fontsize': 10})
# axarr[1,1].text(0.2, 1.03, 'Shallow MHWs Sf', transform=axarr[1,1].transAxes, fontsize=4, fontname='Times New Roman')

axarr[1,2].imshow(data23, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,2].set_title('Reversed MHWs Sf',fontdict={'fontsize': 10})
# axarr[1,2].text(0.2, 1.03, 'Reversed MHWs Sf', transform=axarr[1,2].transAxes, fontsize=4, fontname='Times New Roman')

axarr[1,3].imshow(data24, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,3].set_title('Intensified MHWs Sf',fontdict={'fontsize': 10})
# axarr[1,3].text(0.2, 1.03, 'Intensified MHWs Sf', transform=axarr[1,3].transAxes, fontsize=4, fontname='Times New Roman')

axarr[1,4].imshow(data25, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,4].set_title('Deep MHWs Sf',fontdict={'fontsize': 10})
# axarr[1,4].text(0.25, 1.03, 'Deep MHWs Sf', transform=axarr[1,4].transAxes, fontsize=4, fontname='Times New Roman')

axarr[1,5].imshow(data26, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[1,5].set_title('Intensified_Reversed MHWs Sf',fontdict={'fontsize': 10})
# axarr[1,5].text(0.04, 1.03, 'Intensified_Reversed MHWs Sf', transform=axarr[1,5].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,0].imshow(data31, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,0].set_title('Adv', fontdict={'fontsize': 10})
# axarr[2,0].text(0.5, 1.03, 'Adv', transform=axarr[2,0].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,1].imshow(data32, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,1].set_title('Shallow MHWs Adv',fontdict={'fontsize': 10})
# axarr[2,1].text(0.2, 1.03, 'Shallow MHWs Adv', transform=axarr[2,1].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,2].imshow(data33, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,2].set_title('Reversed MHWs Adv',fontdict={'fontsize': 10})
# axarr[2,2].text(0.2, 1.03, 'Reversed MHWs Adv', transform=axarr[2,2].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,3].imshow(data34, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,3].set_title('Intensified MHWs Adv',fontdict={'fontsize': 10})
# axarr[2,3].text(0.2, 1.03, 'Intensified MHWs Adv', transform=axarr[2,3].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,4].imshow(data35, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,4].set_title('Deep MHWs Adv',fontdict={'fontsize': 10})
# axarr[2,4].text(0.25, 1.03, 'Deep MHWs Adv', transform=axarr[2,4].transAxes, fontsize=4, fontname='Times New Roman')

axarr[2,5].imshow(data36, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[2,5].set_title('Intensified_Reversed MHWs Adv',fontdict={'fontsize': 10})
# axarr[2,5].text(0.04, 1.03, 'Intensified_Reversed MHWs Adv', transform=axarr[2,5].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,0].imshow(data41, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,0].set_title('Res', fontdict={'fontsize': 10})
# axarr[3,0].text(0.5, 1.03, 'Res', transform=axarr[3,0].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,1].imshow(data42, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,1].set_title('Shallow MHWs Res',fontdict={'fontsize': 10})
# axarr[3,1].text(0.2, 1.03, 'Shallow MHWs Res', transform=axarr[3,1].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,2].imshow(data43, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,2].set_title('Reversed MHWs Res',fontdict={'fontsize': 10})
# axarr[3,2].text(0.2, 1.03, 'Reversed MHWs Res', transform=axarr[3,2].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,3].imshow(data44, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,3].set_title('Intensified MHWs Res',fontdict={'fontsize': 10})
# axarr[3,3].text(0.2, 1.03, 'Intensified MHWs Res', transform=axarr[3,3].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,4].imshow(data45, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,4].set_title('Deep MHWs Res',fontdict={'fontsize': 10})
# axarr[3,4].text(0.25, 1.03, 'Deep MHWs Res', transform=axarr[3,4].transAxes, fontsize=4, fontname='Times New Roman')

axarr[3,5].imshow(data46, cmap=cmap_custom, norm=norm_data2, alpha=0.8)
# axarr[3,5].set_title('Intensified_Reversed MHWs Res',fontdict={'fontsize': 10})
# axarr[3,5].text(0.04, 1.03, 'Intensified_Reversed MHWs Res', transform=axarr[3,5].transAxes, fontsize=4, fontname='Times New Roman')

# plt.suptitle('Intensified_Reversed MHWs Percentage', fontsize=10.5)

from mpl_toolkits.basemap import Basemap
lon, lat = np.meshgrid(np.linspace(105, 125, 240), np.linspace(25, 5, 240))

m1 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,0])
m2 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,1])
m3 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,2])
m4 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,3])
m5 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,4])
m6 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[0,5])

m1.drawcoastlines(linewidth=0.5)
m1.drawcountries()
m1.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=2)
m1.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=2)

x, y = m1(lon, lat)
m1.pcolormesh(x,y,data1, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m2.drawcoastlines(linewidth=0.5)
m2.drawcountries()
m2.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m2.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

#
x, y = m2(lon, lat)
m2.pcolormesh(x,y,data2, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m3.drawcoastlines(linewidth=0.5)
m3.drawcountries()
m3.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m3.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m3(lon, lat)
m3.pcolormesh(x,y,data3, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m4.drawcoastlines(linewidth=0.5)
m4.drawcountries()
m4.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m4.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m4(lon, lat)
m4.pcolormesh(x,y,data4, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m5.drawcoastlines(linewidth=0.5)
m5.drawcountries()
m5.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m5.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m5(lon, lat)
m5.pcolormesh(x,y,data5, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m6.drawcoastlines(linewidth=0.5)
m6.drawcountries()
m6.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m6.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m6(lon, lat)
m6.pcolormesh(x,y,data6, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

axarr[0,0].text(-0.1, 1.03, 'a1', transform=axarr[0,0].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,0].text(0.1, 0.88, 'Tt', transform=axarr[0,0].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[0,1].text(-0.1, 1.03, 'b1', transform=axarr[0,1].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,1].text(0.1, 0.88, 'Tt', transform=axarr[0,1].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[0,2].text(-0.1, 1.03, 'c1', transform=axarr[0,2].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,2].text(0.1, 0.88, 'Tt', transform=axarr[0,2].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[0,3].text(-0.1, 1.03, 'd1', transform=axarr[0,3].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,3].text(0.1, 0.88, 'Tt', transform=axarr[0,3].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[0,4].text(-0.1, 1.03, 'e1', transform=axarr[0,4].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,4].text(0.1, 0.88, 'Tt', transform=axarr[0,4].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[0,5].text(-0.1, 1.03, 'f1', transform=axarr[0,5].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[0,5].text(0.1, 0.88, 'Tt', transform=axarr[0,5].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')


m21 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,0])
m22 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,1])
m23 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,2])
m24 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,3])
m25 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,4])
m26 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[1,5])

m21.drawcoastlines(linewidth=0.5)
m21.drawcountries()
m21.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m21.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m21(lon, lat)
m21.pcolormesh(x,y,data21, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m22.drawcoastlines(linewidth=0.5)
m22.drawcountries()
m22.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m22.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m22(lon, lat)
m22.pcolormesh(x,y,data22, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m23.drawcoastlines(linewidth=0.5)
m23.drawcountries()
m23.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m23.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m23(lon, lat)
m23.pcolormesh(x,y,data23, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m24.drawcoastlines(linewidth=0.5)
m24.drawcountries()
m24.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m24.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m24(lon, lat)
m24.pcolormesh(x,y,data24, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m25.drawcoastlines(linewidth=0.5)
m25.drawcountries()
m25.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m25.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m25(lon, lat)
m25.pcolormesh(x,y,data25, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m26.drawcoastlines(linewidth=0.5)
m26.drawcountries()
m26.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m26.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m26(lon, lat)
m26.pcolormesh(x,y,data26, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


axarr[1,0].text(-0.1, 1.03, 'a2', transform=axarr[1,0].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,0].text(0.1, 0.88, 'Sf', transform=axarr[1,0].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[1,1].text(-0.1, 1.03, 'b2', transform=axarr[1,1].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,1].text(0.1, 0.88, 'Sf', transform=axarr[1,1].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[1,2].text(-0.1, 1.03, 'c2', transform=axarr[1,2].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,2].text(0.1, 0.88, 'Sf', transform=axarr[1,2].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[1,3].text(-0.1, 1.03, 'd2', transform=axarr[1,3].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,3].text(0.1, 0.88, 'Sf', transform=axarr[1,3].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[1,4].text(-0.1, 1.03, 'e2', transform=axarr[1,4].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,4].text(0.1, 0.88, 'Sf', transform=axarr[1,4].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[1,5].text(-0.1, 1.03, 'f2', transform=axarr[1,5].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[1,5].text(0.1, 0.88, 'Sf', transform=axarr[1,5].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

m31 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,0])
m32 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,1])
m33 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,2])
m34 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,3])
m35 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,4])
m36 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[2,5])

m31.drawcoastlines(linewidth=0.5)
m31.drawcountries()
m31.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m31.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m31(lon, lat)
m31.pcolormesh(x,y,data31, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m32.drawcoastlines(linewidth=0.5)
m32.drawcountries()
m32.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m32.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m32(lon, lat)
m32.pcolormesh(x,y,data32, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m33.drawcoastlines(linewidth=0.5)
m33.drawcountries()
m33.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m33.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m33(lon, lat)
m33.pcolormesh(x,y,data33, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m34.drawcoastlines(linewidth=0.5)
m34.drawcountries()
m34.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m34.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m34(lon, lat)
m34.pcolormesh(x,y,data34, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m35.drawcoastlines(linewidth=0.5)
m35.drawcountries()
m35.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m35.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m35(lon, lat)
m35.pcolormesh(x,y,data35, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m36.drawcoastlines(linewidth=0.5)
m36.drawcountries()
m36.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m36.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m36(lon, lat)
m36.pcolormesh(x,y,data36, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

axarr[2,0].text(-0.1, 1.03, 'a3', transform=axarr[2,0].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,0].text(0.1, 0.88, 'Adv', transform=axarr[2,0].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[2,1].text(-0.1, 1.03, 'b3', transform=axarr[2,1].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,1].text(0.1, 0.88, 'Adv', transform=axarr[2,1].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[2,2].text(-0.1, 1.03, 'c3', transform=axarr[2,2].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,2].text(0.1, 0.88, 'Adv', transform=axarr[2,2].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[2,3].text(-0.1, 1.03, 'd3', transform=axarr[2,3].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,3].text(0.1, 0.88, 'Adv', transform=axarr[2,3].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[2,4].text(-0.1, 1.03, 'e3', transform=axarr[2,4].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,4].text(0.1, 0.88, 'Adv', transform=axarr[2,4].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[2,5].text(-0.1, 1.03, 'f3', transform=axarr[2,5].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[2,5].text(0.1, 0.88, 'Adv', transform=axarr[2,5].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

m41 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,0])
m42 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,1])
m43 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,2])
m44 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,3])
m45 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,4])
m46 = Basemap(projection='merc', llcrnrlon=105, urcrnrlon=125, llcrnrlat=5, urcrnrlat=25,
            resolution='l', ax=axarr[3,5])

m41.drawcoastlines(linewidth=0.5)
m41.drawcountries()
m41.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m41.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m41(lon, lat)
m41.pcolormesh(x,y,data41, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m42.drawcoastlines(linewidth=0.5)
m42.drawcountries()
m42.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m42.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m42(lon, lat)
m42.pcolormesh(x,y,data42, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m43.drawcoastlines(linewidth=0.5)
m43.drawcountries()
m43.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m43.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m43(lon, lat)
m43.pcolormesh(x,y,data43, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m44.drawcoastlines(linewidth=0.5)
m44.drawcountries()
m44.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m44.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m44(lon, lat)
m44.pcolormesh(x,y,data44, cmap=cmap_custom, norm=norm_data2, alpha=0.8)

m45.drawcoastlines(linewidth=0.5)
m45.drawcountries()
m45.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m45.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m45(lon, lat)
m45.pcolormesh(x,y,data45, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


m46.drawcoastlines(linewidth=0.5)
m46.drawcountries()
m46.drawparallels(np.arange(5, 25, 241), linewidth=0.5, color='k', fontsize=8)
m46.drawmeridians(np.arange(105, 125, 241),  linewidth=0.5, color='k', fontsize=8)

x, y = m46(lon, lat)
m46.pcolormesh(x,y,data46, cmap=cmap_custom, norm=norm_data2, alpha=0.8)


axarr[3,0].text(-0.1, 1.03, 'a4', transform=axarr[3,0].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,0].text(0.1, 0.88, 'Res', transform=axarr[3,0].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[3,1].text(-0.1, 1.03, 'b4', transform=axarr[3,1].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,1].text(0.1, 0.88, 'Res', transform=axarr[3,1].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[3,2].text(-0.1, 1.03, 'c4', transform=axarr[3,2].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,2].text(0.1, 0.88, 'Res', transform=axarr[3,2].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[3,3].text(-0.1, 1.03, 'd4', transform=axarr[3,3].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,3].text(0.1, 0.88, 'Res', transform=axarr[3,3].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[3,4].text(-0.1, 1.03, 'e4', transform=axarr[3,4].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,4].text(0.1, 0.88, 'Res', transform=axarr[3,4].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')

axarr[3,5].text(-0.1, 1.03, 'f4', transform=axarr[3,5].transAxes, fontsize=6, fontweight='bold', fontname='Times New Roman')
axarr[3,5].text(0.1, 0.88, 'Res', transform=axarr[3,5].transAxes, fontsize=8, fontweight='bold', fontname='Times New Roman')


plt.show()

plt.savefig('./my_plot.png')
