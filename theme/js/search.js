/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

/**
 * Search functionality for Products and Projects
 * Allows bidirectional search: find products used in projects, and projects using specific products
 * Enhanced: When searching for a project, shows all glass types used in that project
 */

// Load data from JSON file
let productsData = [];
let projectsData = [];
let basePath = ''; // Base path for images and links

// Load data when page loads
document.addEventListener('DOMContentLoaded', function () {
    // Determine base path based on current URL
    const currentPath = window.location.pathname;
    if (currentPath.includes('/en/')) {
        basePath = '../';
    } else {
        basePath = '';
    }

    loadData();
});

// Load JSON data - Check for different paths based on page location
function loadData() {
    // Try different paths for data.json
    const paths = ['js/data.json', '../js/data.json', '../../js/data.json'];

    tryLoadData(paths, 0);
}

function tryLoadData(paths, index) {
    if (index >= paths.length) {
        console.error('Could not load data.json from any path');
        return;
    }

    fetch(paths[index])
        .then(response => {
            if (!response.ok) throw new Error('Not found');
            return response.json();
        })
        .then(data => {
            productsData = data.products;
            projectsData = data.projects;
            initializeSearch();
        })
        .catch(error => {
            tryLoadData(paths, index + 1);
        });
}

// Initialize search functionality
function initializeSearch() {
    // Add search bar to projects page
    if (document.getElementById('projects-section')) {
        addSearchBarToProjects();
        addAutoComplete();
    }

    // Add search bar to products page
    if (document.getElementById('products-section')) {
        addSearchBarToProducts();
    }
}

// Add autocomplete functionality for projects search
function addAutoComplete() {
    const searchInput = document.getElementById('project-search-input');
    if (!searchInput) return;

    // Create autocomplete dropdown
    const autocompleteDiv = document.createElement('div');
    autocompleteDiv.id = 'project-autocomplete';
    autocompleteDiv.className = 'autocomplete-dropdown';
    searchInput.parentNode.appendChild(autocompleteDiv);

    // Add input event listener for autocomplete
    searchInput.addEventListener('input', function () {
        const value = this.value.toLowerCase().trim();
        autocompleteDiv.innerHTML = '';

        if (value.length < 2) {
            autocompleteDiv.style.display = 'none';
            return;
        }

        // Find matching projects
        const matches = projectsData.filter(project =>
            project.name.toLowerCase().includes(value)
        ).slice(0, 5);

        if (matches.length > 0) {
            autocompleteDiv.style.display = 'block';
            matches.forEach(project => {
                const item = document.createElement('div');
                item.className = 'autocomplete-item';
                item.innerHTML = `
                    <strong>${project.name}</strong>
                    <small>${project.products.length} loại kính</small>
                `;
                item.addEventListener('click', function () {
                    searchInput.value = project.name;
                    autocompleteDiv.style.display = 'none';
                    searchProjects();
                });
                autocompleteDiv.appendChild(item);
            });
        } else {
            autocompleteDiv.style.display = 'none';
        }
    });

    // Hide autocomplete when clicking outside
    document.addEventListener('click', function (e) {
        if (!searchInput.contains(e.target) && !autocompleteDiv.contains(e.target)) {
            autocompleteDiv.style.display = 'none';
        }
    });
}

// Add search bar to projects page
function addSearchBarToProjects() {
    const searchInput = document.getElementById('project-search-input');
    const searchBtn = document.getElementById('project-search-btn');

    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', searchProjects);
        searchInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                searchProjects();
                // Hide autocomplete
                const autocomplete = document.getElementById('project-autocomplete');
                if (autocomplete) autocomplete.style.display = 'none';
            }
        });
    }
}

// Add search bar to products page
function addSearchBarToProducts() {
    const searchInput = document.getElementById('product-search-input');
    const searchBtn = document.getElementById('product-search-btn');

    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', searchProducts);
        searchInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                searchProducts();
            }
        });
    }
}

// Search projects and filter the project list
function searchProjects() {
    const searchTerm = document.getElementById('project-search-input').value.toLowerCase().trim();
    const resultsDiv = document.getElementById('search-results');
    const filtrContainer = document.querySelector('.filtr-container');
    const portfolioFilter = document.querySelector('.portfolio-filter');
    const projectsSection = document.getElementById('projects-section');

    if (!filtrContainer) return;

    // Clear previous search results message
    resultsDiv.innerHTML = '';

    if (!searchTerm) {
        // Show all projects - restore original view
        resetSearchView();
        return;
    }

    // Hide the original project grid and filter buttons
    filtrContainer.classList.add('search-active');
    if (portfolioFilter) {
        portfolioFilter.style.display = 'none';
    }
    if (projectsSection) {
        projectsSection.classList.add('search-active-mode');
    }

    // Hide the row containing the project grid
    const parentRow = filtrContainer.closest('.row');
    if (parentRow) {
        parentRow.classList.add('search-active-row');
    }

    // Find matching projects by name or description
    const matchingProjectsByName = projectsData.filter(project =>
        project.name.toLowerCase().includes(searchTerm) ||
        project.description.toLowerCase().includes(searchTerm)
    );

    // Find matching products
    const matchingProducts = productsData.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm)
    );

    // Get project IDs to show
    let projectIdsToShow = new Set();

    // Add projects matched by name/description
    matchingProjectsByName.forEach(project => {
        projectIdsToShow.add(project.id);
    });

    // Add projects that use matching products
    matchingProducts.forEach(product => {
        projectsData.forEach(project => {
            if (project.products.includes(product.id)) {
                projectIdsToShow.add(project.id);
            }
        });
    });

    // Find matching projects from data
    const foundProjects = projectsData.filter(p => projectIdsToShow.has(p.id));

    // Show message if no results
    if (foundProjects.length === 0) {
        resultsDiv.innerHTML = `
            <div class="alert alert-info mt-3">
                <strong>Không tìm thấy dự án nào.</strong>
                <button type="button" class="btn btn-sm btn-outline-primary ml-3" onclick="clearProjectSearch()">
                    <i class="tf-ion-android-refresh"></i> Xem tất cả dự án
                </button>
            </div>
        `;
        // Hide products section
        const productsSectionEl = document.getElementById('project-products-section');
        if (productsSectionEl) {
            productsSectionEl.innerHTML = '';
        }
    } else {
        // Show clear search button in results
        resultsDiv.innerHTML = `
            <div class="search-result-header">
                <span class="search-result-text">Tìm thấy <strong>${foundProjects.length}</strong> dự án</span>
                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="clearProjectSearch()">
                    <i class="tf-ion-android-close"></i> Xóa tìm kiếm
                </button>
            </div>
        `;
        // Display enhanced results showing products used in each project
        displayEnhancedProjectResults(foundProjects);
    }
}

// Reset search view to show all projects
function resetSearchView() {
    const filtrContainer = document.querySelector('.filtr-container');
    const portfolioFilter = document.querySelector('.portfolio-filter');
    const projectsSection = document.getElementById('projects-section');
    const productsSection = document.getElementById('project-products-section');
    const resultsDiv = document.getElementById('search-results');

    // Show filter container
    if (filtrContainer) {
        filtrContainer.classList.remove('search-active');
        const allItems = filtrContainer.querySelectorAll('.filtr-item');
        allItems.forEach(item => {
            item.style.display = '';
        });
        const parentRow = filtrContainer.closest('.row');
        if (parentRow) {
            parentRow.classList.remove('search-active-row');
        }
    }

    // Show portfolio filter buttons
    if (portfolioFilter) {
        portfolioFilter.style.display = '';
    }

    // Remove search mode class
    if (projectsSection) {
        projectsSection.classList.remove('search-active-mode');
    }

    // Clear products section
    if (productsSection) {
        productsSection.innerHTML = '';
    }

    // Clear results div
    if (resultsDiv) {
        resultsDiv.innerHTML = '';
    }
}

// Clear project search function (called by button)
function clearProjectSearch() {
    const searchInput = document.getElementById('project-search-input');
    if (searchInput) {
        searchInput.value = '';
    }
    resetSearchView();
}

// Enhanced display: Show each project with its glass types
function displayEnhancedProjectResults(projects) {
    const productsSection = document.getElementById('project-products-section');
    if (!productsSection) return;

    if (projects.length === 0) {
        productsSection.innerHTML = '';
        return;
    }

    // Determine text based on language
    const isEnglish = window.location.pathname.includes('/en/');
    const texts = {
        glassUsed: isEnglish ? 'types of glass used' : 'loại kính được sử dụng',
        viewProjectDetail: isEnglish ? 'View Project Details' : 'Xem chi tiết dự án',
        glassTypesTitle: isEnglish ? 'Glass Types Used' : 'Các loại kính được sử dụng',
        viewDetail: isEnglish ? 'View Details' : 'Xem chi tiết'
    };

    let html = '';

    // For each found project, display its glass types
    projects.forEach((project, index) => {
        // Get products for this project
        const projectProducts = project.products.map(productId => {
            return productsData.find(p => p.id === productId);
        }).filter(p => p !== undefined);

        // Get project link with basePath
        const projectLink = basePath + (project.link || `projects/${project.id}.html`);
        // Get project image with basePath
        const projectImage = basePath + project.image;

        html += `
            <div class="col-12 project-result-section ${index > 0 ? 'mt-5' : ''}">
                <div class="project-glass-header">
                    <div class="row align-items-center">
                        <!-- Project Image -->
                        <div class="col-lg-4 col-md-5 mb-4 mb-md-0">
                            <a href="${projectLink}" class="project-image-link">
                                <div class="project-image-wrapper">
                                    <img loading="lazy" src="${projectImage}" alt="${project.name}" class="project-result-image">
                                    <div class="project-image-overlay">
                                        <span class="view-project-btn">
                                            <i class="tf-ion-ios-search-strong"></i>
                                            <span>${texts.viewProjectDetail}</span>
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                        <!-- Project Info -->
                        <div class="col-lg-8 col-md-7">
                            <div class="project-info-box">
                                <h3 class="project-result-title">
                                    <a href="${projectLink}">
                                        <i class="tf-ion-android-pin"></i> ${project.name}
                                    </a>
                                </h3>
                                <p class="project-result-desc">${project.description}</p>
                                <div class="project-glass-count">
                                    <span class="glass-count-badge">${projectProducts.length}</span>
                                    <span class="glass-count-text">${texts.glassUsed}</span>
                                </div>
                                <a href="${projectLink}" class="btn btn-main btn-sm mt-3">
                                    <i class="tf-ion-ios-arrow-thin-right"></i> ${texts.viewProjectDetail}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="glass-types-container">
                    <h4 class="glass-section-title">
                        <i class="tf-ion-ios-box"></i> ${texts.glassTypesTitle}
                    </h4>
                    <div class="row">
        `;

        projectProducts.forEach(product => {
            // Get product image and link with basePath
            const productImage = basePath + product.image;
            const productLink = basePath + product.link;
            const fallbackImage = basePath + 'images/products/kinhcuongluc.jpg';

            html += `
                <div class="col-lg-3 col-md-4 col-sm-6 mb-4">
                    <div class="glass-type-card">
                        <div class="glass-card-image">
                            <img loading="lazy" src="${productImage}" alt="${product.name}" onerror="this.src='${fallbackImage}'">
                            <div class="glass-card-overlay">
                                <a href="${productLink}" class="glass-view-btn">
                                    <i class="tf-ion-ios-search-strong"></i>
                                </a>
                            </div>
                        </div>
                        <div class="glass-card-content">
                            <h5><a href="${productLink}">${product.name}</a></h5>
                            <p>${product.description.substring(0, 80)}...</p>
                            <a href="${productLink}" class="btn-glass-detail">
                                ${texts.viewDetail} <i class="tf-ion-ios-arrow-thin-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            `;
        });

        html += `
                    </div>
                </div>
            </div>
        `;
    });

    // Add summary section if multiple projects
    if (projects.length > 1) {
        // Collect all unique products
        const allProductIds = new Set();
        projects.forEach(project => {
            project.products.forEach(productId => {
                allProductIds.add(productId);
            });
        });

        html += `
            <div class="col-12 mt-5">
                <div class="search-summary-box">
                    <h4><i class="tf-ion-ios-analytics"></i> Tổng kết tìm kiếm</h4>
                    <div class="summary-stats">
                        <div class="stat-item">
                            <span class="stat-number">${projects.length}</span>
                            <span class="stat-label">Dự án</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">${allProductIds.size}</span>
                            <span class="stat-label">Loại kính được sử dụng</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    productsSection.innerHTML = html;

    // Add scroll to results
    productsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Search products and filter projects on products page
function searchProducts() {
    const searchTerm = document.getElementById('product-search-input').value.toLowerCase().trim();
    const resultsDiv = document.getElementById('product-search-results');

    // Clear previous search results message
    resultsDiv.innerHTML = '';

    if (!searchTerm) {
        return;
    }

    // Find matching products
    const matchingProducts = productsData.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm)
    );

    // Find matching projects by name or description
    const matchingProjectsByName = projectsData.filter(project =>
        project.name.toLowerCase().includes(searchTerm) ||
        project.description.toLowerCase().includes(searchTerm)
    );

    // Get project IDs that use matching products
    let projectIdsToShow = new Set();

    // Add projects matched by name/description
    matchingProjectsByName.forEach(project => {
        projectIdsToShow.add(project.id);
    });

    // Add projects that use matching products
    matchingProducts.forEach(product => {
        projectsData.forEach(project => {
            if (project.products.includes(product.id)) {
                projectIdsToShow.add(project.id);
            }
        });
    });

    // If we're on projects page, filter the projects
    const filtrContainer = document.querySelector('.filtr-container');
    if (filtrContainer) {
        // Add search-active class to make container shrink
        filtrContainer.classList.add('search-active');
        // Add search-active-row class to parent row to make it shrink too
        const parentRow = filtrContainer.closest('.row');
        if (parentRow) {
            parentRow.classList.add('search-active-row');
        }

        const allItems = filtrContainer.querySelectorAll('.filtr-item');
        let foundCount = 0;

        allItems.forEach(item => {
            const projectId = item.getAttribute('data-project-id');
            if (projectId && projectIdsToShow.has(projectId)) {
                item.style.display = '';
                foundCount++;
            } else {
                item.style.display = 'none';
            }
        });

        // Show message if no results
        if (foundCount === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info mt-3">Không tìm thấy dự án nào.</div>';
        }
    } else {
        // If not on projects page, show message
        if (projectIdsToShow.size === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info mt-3">Không tìm thấy dự án nào sử dụng sản phẩm này.</div>';
        } else {
            resultsDiv.innerHTML = `<div class="alert alert-success mt-3">Tìm thấy ${projectIdsToShow.size} dự án. Vui lòng vào trang Dự Án để xem chi tiết.</div>`;
        }
    }
}

