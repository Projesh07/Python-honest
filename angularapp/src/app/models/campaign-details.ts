import {Category} from './category';
import {Tag} from './tags';

import {CampaignComment} from './campaign-comment';
import {CampaignDonate} from './campaign-donate';
import {Document} from './document';

export interface CampaignDetails{
  id:number;
  title: string;
  story:string;
  amount:string;
  start_date:string;
  end_date:string;
  status:number;
  publish_date:string;
  category:Category;
  documents:Document[];
  campaign_donate:CampaignDonate[];
  tags:Tag[];
  total_donate:string;
  campaign_comment:CampaignComment[];
  progress:number;
  featured_image:string;
}
