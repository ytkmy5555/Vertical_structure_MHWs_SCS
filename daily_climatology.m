clear;close all;clc;
filename='D:\CARS_Argo\CARS\temperature_cars2009a.nc';
% ncdisp(filename)
lat=ncread(filename,'lat');
lon=ncread(filename,'lon');
depth=ncread(filename,'depth');
depth_ann=ncread(filename,'depth_ann');
depth_semiann=ncread(filename,'depth_semiann');
% 
mean=ncread(filename,'mean');
% 
an_cos=ncread(filename,'an_cos');
% 
an_sin=ncread(filename,'an_sin');
% 
sa_cos=ncread(filename,'sa_cos');
% 半
sa_sin=ncread(filename,'sa_sin');
% 
% E=m+a1×cosα+a2×sinα+a3×cos2α+a4×sin2α,其中α＝2πd/366
% 
% 
% 
clim_lat=lat(161:201);
clim_lon=lon(211:251);
clim_mean=mean(211:251,161:201,:);
clim_ancos=an_cos(211:251,161:201,:);
clim_ansin=an_sin(211:251,161:201,:);
clim_sacos=sa_cos(211:251,161:201,:);
clim_sasin=sa_sin(211:251,161:201,:);
salt=NaN(41,41,55,366);
for i=1:41
    for j=1:41
        for k=1:55
            for d=1:366
                t=2*pi*d/366;
                salt(i,j,k,d)=clim_mean(i,j,k)+clim_ancos(i,j,k)*cos(t)+...
                    clim_ansin(i,j,k)*sin(t)+clim_sacos(i,j,k)*cos(2*t)+...
                    clim_sasin(i,j,k)*sin(2*t);      
            end
        end
    end
end
save D:\CARS_Argo\CARS\clim_temp.mat clim_lat clim_lon depth_semiann salt
% 
% zz=10:10:1000;
% zz=zz';
% clim_salt=NaN(41,41,100,366);
% for i=1:41
%     for j=1:41
%         for k=1:366
%             ss=squeeze(salt(i,j,:,k));
% %             if(~isnan(ss))
%                 s=makima(depth_semiann,ss,zz);
%                 clim_salt(i,j,:,k)=s;
% %             end
%         end
%     end
% end



