import {CampaignComment} from "./campaign-comment";
export interface CommentList{
  count:number;
  next:string;
  previous:string;
  results:CampaignComment[];
}
