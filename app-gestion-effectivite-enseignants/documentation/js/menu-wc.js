'use strict';

customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">app-gestion-effectivite-enseignants documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                                <li class="link">
                                    <a href="properties.html" data-type="chapter-link">
                                        <span class="icon ion-ios-apps"></span>Properties
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-bs-toggle="collapse" ${ isNormalMode ?
                                'data-bs-target="#modules-links"' : 'data-bs-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AdminModule.html" data-type="entity-link" >AdminModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-AdminModule-f8c8c5f3da903cb9653cc021a26f8faf9457055edab5f9de3a7cc5dc7b1ae2ac942b293efb0aa0748d2554b41dd7791d813d9878192c053b42e31a206ddbba0a"' : 'data-bs-target="#xs-components-links-module-AdminModule-f8c8c5f3da903cb9653cc021a26f8faf9457055edab5f9de3a7cc5dc7b1ae2ac942b293efb0aa0748d2554b41dd7791d813d9878192c053b42e31a206ddbba0a"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AdminModule-f8c8c5f3da903cb9653cc021a26f8faf9457055edab5f9de3a7cc5dc7b1ae2ac942b293efb0aa0748d2554b41dd7791d813d9878192c053b42e31a206ddbba0a"' :
                                            'id="xs-components-links-module-AdminModule-f8c8c5f3da903cb9653cc021a26f8faf9457055edab5f9de3a7cc5dc7b1ae2ac942b293efb0aa0748d2554b41dd7791d813d9878192c053b42e31a206ddbba0a"' }>
                                            <li class="link">
                                                <a href="components/AheaderComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AheaderComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/AlayoutComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AlayoutComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CGestionProgrammesComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CGestionProgrammesComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CIndexComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CIndexComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CSuiviEnseignementsComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CSuiviEnseignementsComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CVerificationContenusComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CVerificationContenusComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/DashboardComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >DashboardComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/SidemenuComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >SidemenuComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AdminRoutingModule.html" data-type="entity-link" >AdminRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link" >AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-AppModule-033d59eb0f1bbf0f098ed90397b1f01038a2588dde28b4ec3e395742766db47fbc2a6b241f74c060786ae2c795d2d501df2eedda986d93a97f42dbe8e3665ae4"' : 'data-bs-target="#xs-components-links-module-AppModule-033d59eb0f1bbf0f098ed90397b1f01038a2588dde28b4ec3e395742766db47fbc2a6b241f74c060786ae2c795d2d501df2eedda986d93a97f42dbe8e3665ae4"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-033d59eb0f1bbf0f098ed90397b1f01038a2588dde28b4ec3e395742766db47fbc2a6b241f74c060786ae2c795d2d501df2eedda986d93a97f42dbe8e3665ae4"' :
                                            'id="xs-components-links-module-AppModule-033d59eb0f1bbf0f098ed90397b1f01038a2588dde28b4ec3e395742766db47fbc2a6b241f74c060786ae2c795d2d501df2eedda986d93a97f42dbe8e3665ae4"' }>
                                            <li class="link">
                                                <a href="components/AppComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ErrorComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ErrorComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AppRoutingModule.html" data-type="entity-link" >AppRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/AuthModule.html" data-type="entity-link" >AuthModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-AuthModule-59ac104655f52e0c9e83e83d4361a0882e2e005be5177b13e24cff667c63a772cc677f94568468e3c8c8f8b2bc6137da4a5b09410325462f8cf921c4c23a7020"' : 'data-bs-target="#xs-components-links-module-AuthModule-59ac104655f52e0c9e83e83d4361a0882e2e005be5177b13e24cff667c63a772cc677f94568468e3c8c8f8b2bc6137da4a5b09410325462f8cf921c4c23a7020"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AuthModule-59ac104655f52e0c9e83e83d4361a0882e2e005be5177b13e24cff667c63a772cc677f94568468e3c8c8f8b2bc6137da4a5b09410325462f8cf921c4c23a7020"' :
                                            'id="xs-components-links-module-AuthModule-59ac104655f52e0c9e83e83d4361a0882e2e005be5177b13e24cff667c63a772cc677f94568468e3c8c8f8b2bc6137da4a5b09410325462f8cf921c4c23a7020"' }>
                                            <li class="link">
                                                <a href="components/LoginComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >LoginComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/LogoutComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >LogoutComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AuthRoutingModule.html" data-type="entity-link" >AuthRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/GestionEnseignantsModule.html" data-type="entity-link" >GestionEnseignantsModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/GestionEnseignantsRoutingModule.html" data-type="entity-link" >GestionEnseignantsRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/PublicRoutingModule.html" data-type="entity-link" >PublicRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/PulicModule.html" data-type="entity-link" >PulicModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-PulicModule-d28105e1f7711292211fea71daf46e49b298fa3d18fade1ad3024e5907ed2b8f74336caf117a22e964ce3bd36f74268d6ceeffa4be33774dc75c8c4f695b3476"' : 'data-bs-target="#xs-components-links-module-PulicModule-d28105e1f7711292211fea71daf46e49b298fa3d18fade1ad3024e5907ed2b8f74336caf117a22e964ce3bd36f74268d6ceeffa4be33774dc75c8c4f695b3476"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-PulicModule-d28105e1f7711292211fea71daf46e49b298fa3d18fade1ad3024e5907ed2b8f74336caf117a22e964ce3bd36f74268d6ceeffa4be33774dc75c8c4f695b3476"' :
                                            'id="xs-components-links-module-PulicModule-d28105e1f7711292211fea71daf46e49b298fa3d18fade1ad3024e5907ed2b8f74336caf117a22e964ce3bd36f74268d6ceeffa4be33774dc75c8c4f695b3476"' }>
                                            <li class="link">
                                                <a href="components/GestionEnseignantComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GestionEnseignantComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HomeComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HomeComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/PheaderComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >PheaderComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/PlayoutComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >PlayoutComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/UserModule.html" data-type="entity-link" >UserModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-UserModule-4c256b50acbc91a634f095f935d57e9975b49fbcf1e163644cd179562de7dd0670c9f058d813f5e2099198c29948c712be97aabf23af92fb5730bec7ad9f3810"' : 'data-bs-target="#xs-components-links-module-UserModule-4c256b50acbc91a634f095f935d57e9975b49fbcf1e163644cd179562de7dd0670c9f058d813f5e2099198c29948c712be97aabf23af92fb5730bec7ad9f3810"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-UserModule-4c256b50acbc91a634f095f935d57e9975b49fbcf1e163644cd179562de7dd0670c9f058d813f5e2099198c29948c712be97aabf23af92fb5730bec7ad9f3810"' :
                                            'id="xs-components-links-module-UserModule-4c256b50acbc91a634f095f935d57e9975b49fbcf1e163644cd179562de7dd0670c9f058d813f5e2099198c29948c712be97aabf23af92fb5730bec7ad9f3810"' }>
                                            <li class="link">
                                                <a href="components/UAddComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >UAddComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UDeleteComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >UDeleteComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UEditComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >UEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UIndexComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >UIndexComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/UserRoutingModule.html" data-type="entity-link" >UserRoutingModule</a>
                            </li>
                </ul>
                </li>
                        <li class="chapter">
                            <a data-type="chapter-link" href="routes.html"><span class="icon ion-ios-git-branch"></span>Routes</a>
                        </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank" rel="noopener noreferrer">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});