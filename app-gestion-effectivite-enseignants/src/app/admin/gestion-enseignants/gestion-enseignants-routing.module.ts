import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CIndexComponent } from './c-index/c-index.component';
import { CGestionProgrammesComponent } from './c-gestion-programmes/c-gestion-programmes.component';
import { CSuiviEnseignementsComponent } from './c-suivi-enseignements/c-suivi-enseignements.component';
import { CVerificationContenusComponent } from './c-verification-contenus/c-verification-contenus.component';

const routes: Routes = [
  {path: '', component: CIndexComponent},
  {path: 'gestion', component: CGestionProgrammesComponent},
  {path: 'suivi', component: CSuiviEnseignementsComponent},
  {path: 'verification', component: CVerificationContenusComponent}
  
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class GestionEnseignantsRoutingModule { }
