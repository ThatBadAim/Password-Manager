with open('CipherVault/MainWindow.xaml', 'r') as f:
    content = f.read()

search = '''                            <Grid>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0"/>
                                <TextBox Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>'''
replace = '''                            <Grid>
                                <TextBlock Text="&#xE1A3;" FontFamily="Segoe MDL2 Assets" Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="4,0,0,0"/>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0">
                                    <TextBlock.Style>
                                        <Style TargetType="TextBlock">
                                            <Setter Property="Visibility" Value="Collapsed"/>
                                            <Style.Triggers>
                                                <DataTrigger Binding="{Binding Text.Length, ElementName=SearchBox}" Value="0">
                                                    <Setter Property="Visibility" Value="Visible"/>
                                                </DataTrigger>
                                            </Style.Triggers>
                                        </Style>
                                    </TextBlock.Style>
                                </TextBlock>
                                <TextBox x:Name="SearchBox" Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>'''

content = content.replace(search, replace)

with open('CipherVault/MainWindow.xaml', 'w') as f:
    f.write(content)
