import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {UserDashboardComponent} from "./pages/user-dashboard/user-dashboard.component";
import {UserDashboardStatComponent} from "./components/user-dashboard-stat/user-dashboard-stat.component";
import {UserProfileComponent} from "./components/user-profile/user-profile.component";
import {UserDonationHistoryComponent} from "./components/user-donation-history/user-donation-history.component";
import {UserRecentDonationComponent} from "./components/user-recent-donation/user-recent-donation.component";

const routes: Routes = [
  {
    path: '', component: UserDashboardComponent,
    children: [
      { path: 'dashboard', component: UserDashboardStatComponent },
      { path: 'profile', component: UserProfileComponent },
      { path: 'donation-history', component: UserDonationHistoryComponent },
      { path: 'recent-donation', component: UserRecentDonationComponent },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
