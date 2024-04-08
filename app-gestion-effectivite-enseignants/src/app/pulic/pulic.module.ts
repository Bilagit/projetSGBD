import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { PublicRoutingModule } from './public-routing.module';
import { PlayoutComponent } from './playout/playout.component';
import { GestionEnseignantComponent } from './gestion-enseignant/gestion-enseignant.component';
import { PheaderComponent } from './pheader/pheader.component';



@NgModule({
  declarations: [
    HomeComponent,
    PlayoutComponent,
    GestionEnseignantComponent,
    PheaderComponent
  ],
  imports: [
    CommonModule,
    PublicRoutingModule
  ]
})
export class PulicModule { }
