import {UserDetails} from './user-details';

export interface CampaignComment{
	id:string;
	comment:string;
	comment_at:string;
	created_at:string;
	updated_at:string;
	user:UserDetails;
	campaign:Number;
}


