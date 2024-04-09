import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AdminRoutingModule } from './admin-routing.module';
import { AlayoutComponent } from './alayout/alayout.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SidemenuComponent } from './sidemenu/sidemenu.component';
import { CIndexComponent } from './gestion-enseignants/c-index/c-index.component';
import { CSuiviEnseignementsComponent } from './gestion-enseignants/c-suivi-enseignements/c-suivi-enseignements.component';
import { CGestionProgrammesComponent } from './gestion-enseignants/c-gestion-programmes/c-gestion-programmes.component';
import { CVerificationContenusComponent } from './gestion-enseignants/c-verification-contenus/c-verification-contenus.component';
import { AheaderComponent } from './aheader/aheader.component';


@NgModule({
  declarations: [
    AlayoutComponent,
    DashboardComponent,
    SidemenuComponent,
    CIndexComponent,
    CSuiviEnseignementsComponent,
    CGestionProgrammesComponent,
    CVerificationContenusComponent,
    AheaderComponent
  ],
  imports: [
    CommonModule,
    AdminRoutingModule
  ]
})
export class AdminModule { }
