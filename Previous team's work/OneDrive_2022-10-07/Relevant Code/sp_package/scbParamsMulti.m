function [cfg] = scbParamsMulti(file)
%%
cfg.sdir = 'C:\Users\angela.henricks\Desktop\Research\MatlabAnalysis\MIA\MIAwAlcInj\POST';

% file = 'H10RegChowNov23';
cfg.file = file;
cfg.nFilt = [57 63];
cfg.dsf = 5;
cfg.thresh = 1.5; 
cfg.onset = 0.0125;
cfg.offset = 0.5;
cfg.foi = [1 1 100];
cfg.bands = {'delta',[1,4];
             'theta',[5,10];
             'alpha',[11,14];
             'beta',[15,30];
             'lgamma',[45,65];
             'hgamma',[70,90]};
cfg.overlap = 0.5;
cfg.cohMethod = 'mtm';
cfg.skip = [];
%cfg.eoi = [{'Base1',[0,5]};{'Base2',[0,5]};{'Stim1',[0,5]}];
% cfg.eoi = [{'Base1',[0,5]};{'Base2',[0,5]};{'Base3',[0,5]};...
%     {'Base4',[0,5]};{'Base5',[0,5]};{'Base6',[0,5]};{'Base7',[0,5]};...
%     {'Base8',[0,5]};{'Stim1',[0,5]};{'Stim2',[0,5]};{'Stim3',[0,5]};...
%     {'Stim4',[0,5]};{'Stim5',[0,5]};{'Stim6',[0,5]};{'Stim7',[0,5]}]; 
% cfg.eoi = [{'binge (s'},[-4,1];{'binge (s'},[-3,2];{'binge (s'},[-2,3];...
%     {'binge (s'},[-1,4]];
% cfg.eoi = {'rest',[0 3]};
% cfg.eoi = {'~Both',[0 5]};
% cfg.eoi = {'water',[0 5];'alcohol',[0 5]};
cfg.eoi = {'all',[0 5]};
% cfg.eoi = [{'Baseline',[0 5]};{'Saline0min',[0 5]};{'Saline10min',[0 5]};{'Saline20min',[0 5]}];
% cfg.eoi = [{'THC0min',[0 5]};{'THC10min',[0 5]};{'THC20min',[0 5]};{'THC30min',[0 5]};{'THC40min',[0 5]};...
%    {'THC50min',[0 5]};{'THC60min',[0 5]};{'THC70min',[0 5]};{'THC80min',[0 5]}];
%  cfg.eoi = [{'Baseline',[0 5]};{'Saline0min',[0 5]};{'Saline10min',[0 5]};{'Saline20min',[0 5]};...
%      {'Cocaine0min',[0 5]};{'Cocaine10min',[0 5]};{'Cocaine20min',[0 5]};{'Cocaine30min',[0 5]};{'Cocaine40min',[0 5]};...
%      {'Cocaine50min',[0 5]};{'Cocaine60min',[0 5]};{'Cocaine70min',[0 5]};{'Cocaine80min',[0 5]}];
% cfg.eoi = [{'Baseline',[0 5]};{'Saline0min',[0 5]};{'Saline10min',[0 5]};{'Saline20min',[0 5]};...
%    {'Cocaine0min',[0 5]};{'Cocaine10min',[0 5]};{'Cocaine20min',[0 5]};{'Cocaine30min',[0 5]};{'Cocaine40min',[0 5]};...
%{'Cocaine50min',[0 5]};{'Cocaine60min',[0 5]};{'Cocaine70min',[0 5]};{'Cocaine80min',[0 5]};...
%    {'Cocaine90min',[0 5]};{'Cocaine100min',[0 5]};{'Cocaine110min',[0 5]};{'Cocaine120min',[0 5]};...
%    {'Cocaine130min',[0 5]};{'Cocaine140min',[0 5]};{'Cocaine150min',[0 5]};{'Cocaine160min',[0 5]};...
%    {'Cocaine170min',[0 5]}];
% cfg.eoi = {'Baseline',[0 5]};
% cfg.eoi = {'Cocaine20',[0 5]};
% cfg.eoi = {'Cocaine',[0 5]};
% cfg.eoi = {'Inter',[0 5]};
% cfg.eoi = {'pre',[0 5];'post',[0 5]};
% cfg.eoi = {'drink',[0 5];'~drink',[0 5]};
% cfg.eoi = {'~drink',[0 5]};
% cfg.eoi = {'trial',[-5 0]};
% for ii = 1:240
%    cfg.eoi(ii,:) = {'binge (s',[-4-ii 1-ii]}; 
% end
% cfg.eoi(end+1,:) = {'~binge',[0 5]};
% for ii = 1:2
%     eoi = [eoi;{['Base',num2str(ii),' '],[0 5]}];
% end
% for ii = 1
%    eoi = [eoi;{['Inter',num2str(ii),' '],[0,5]}]; 
% end
% eoi = {'base',[0 5];'post',[0 5]};
% eoi = {'drink',[0 5];'~drink',[0 5]};
% eoi = {'rest',[0 5]};
% eoi = {'Base',[0 5];'Int1',[0 5];'Int2',[0 5];'Int3',[0 5];'Int4',[0 5];'Int5',[0 5];'Post',[0 5]};
% eoi = {'binge',[0 5];'notbinge',[0 5]};

% Pre Drinking
% for ii = 1:61
%    eoi(ii,:) = {'drink (s',[-4-ii 1-ii]}; 
% end

% Post Drinking
% for ii = 1:61
%    eoi(ii,:) = {'drink (e',[ii-1 ii+4]}; 
% end

% 15 seconds pre and post drink and 5 seconds at beginning and end of drink
% for ii = 1:16
%    eoi(ii,:) = {'drink (s',[-ii+1 6-ii]}; 
% end
% for ii = 1:16
%     eoi(ii+16,:) = {'drink (e',[ii-6 ii-1]};
% end
cfg.vis = 'n';
cfg.saveParent = 'C:\Users\angela.henricks\Desktop\Research\MatlabAnalysis\MIA\MIAwAlcInj\POST\processed\';
% cfg.saveParent = 'E:\aaberg\processedNew\';
% cfg.saveParent = 'C:\Users\GreenLab\Desktop\Diana\Cocaine\bins\C3\processed';
% cfg.saveParent = 'C:\Users\Pythia\Documents\GreenLab\data\angelaK\processed\'