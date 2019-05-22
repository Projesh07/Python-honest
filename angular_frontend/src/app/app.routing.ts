import {ModuleWithProviders} from "@angular/core";
import {Routes, RouterModule} from "@angular/router";

import { HomeComponentComponent } from './home-component/home-component.component';
import { CampaignComponentComponent } from './campaign-component/campaign-component.component';
import { CampaingnPageComponent } from './campaingn-page/campaingn-page.component';
import { RegistrationComponentComponent } from './registration-component/registration-component.component';
import { LoginComponent } from './login/login.component';
import { UserProfileComponent } from './user-profile/user-profile.component';

const appRoutes : Routes = [
    {   
        path:'',
        component: HomeComponentComponent,
        pathMatch: 'full'
    },
    {
        path:'categories/:id',
        component: CampaignComponentComponent,
        pathMatch: 'full'
    },
    {
        path:'campdetails/:slug',
        component: CampaingnPageComponent,
        pathMatch: 'full'
    },

    {
        path:'registration',
        component: RegistrationComponentComponent,
        pathMatch: 'full'
    },

    {
        path:'login',
        component: LoginComponent,
        pathMatch: 'full'
    },

    {
        path:'user-profile',
        component: UserProfileComponent,
        pathMatch: 'full'
    }

];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
