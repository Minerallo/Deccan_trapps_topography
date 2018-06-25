% Lambda=*10e3
% xb=Lamda/2


%% Plot DEM with lower resolution and make lot of profils
%save('etopindia.mat')
clear all;
load('etopindia.mat');
etovect=fliplr(min(etopindia(:,2)):(max(etopindia(:,2))-min(etopindia(:,2)))/249:max(etopindia(:,2)));

for i=1:numel(etovect)
    diffeto=abs(etopindia(:,2)-etovect(i));
    j(i)=find(diffeto==min(diffeto),1);
end

latprof=unique(etopindia(j,2));
%numel(unique(etopindia(j,2)))

for i=1:numel(latprof)
    [k]=find(etopindia(:,2)==latprof(i));
    profiles(i,:)=etopindia(k,3);
end

% figure(1);
% plot(profiles(62,:))

% figure(888)
% surf(profiles); shading interp; colormap(jet)

%% profil flexuration
%Escarpment need to be on west side for calculation
a=1;
% %splitting latprof vector
% numelevec = 40; % block size
% nelem = numel(latprof);
% celem = mat2cell(latprof,diff([0:numelevec:nelem-1,nelem]));
% %zelem = cellfun(@median,celem);

for i=1:numel(latprof)
    [M]=find(profiles(i,:)==max(profiles(i,:)),1);
    indmax(i)=M;
end
[N,X]=hist(indmax);
[E]=find(N==max(N));
diffindX=abs(indmax-X(E)); %definir une tolerance diff<10

tolerance=35
mintol=round(X(E)-tolerance)
maxtol=round(X(E)+tolerance)

for i=1:numel(latprof)
    if diffindX(i)>tolerance
        prof(i,:)=profiles(i,mintol:maxtol);
        [G]=find(profiles(i,:)==max(prof(i,:)),1);
        indmax2(i)=G;
    else
        indmax2(i)=indmax(i);
    end
end
diffindX2=abs(indmax2-X(E))
%works but heavy
% for i=1:numel(latprof)
%     prof(i,:)=profiles(i,:);
%     while diffindX(i)>=tolerance
%         [G]=find(profiles(i,:)==max(prof(i,:)),1);
%         diffindX(i)=abs(G-X(E))
%         if diffindX(i)>=tolerance
%             prof(i,G)=0;
%         else
%             indmax(i)=G;
%         end
%     end
% end


    %maxtopo(i)=profiles(i,M)

    figure(999)
    pcolor(profiles);shading interp; colormap(jet);hold on
    plot(indmax2,1:numel(latprof),'bo')

    %figure(2)
    % hist(maxtopo)
